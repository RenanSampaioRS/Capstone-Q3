from app.models.employees_model import EmployeesModel
from flask import current_app
from flask_restful import reqparse
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from app.services.helpers import add_commit
from app.exc import DuplicatedKeys


def get_employee_by_login(data) -> EmployeesModel:
    user: EmployeesModel = EmployeesModel.query.filter_by(login=data['login']).first()
    return user

def check_cpf(data) -> bool:
    user: EmployeesModel = EmployeesModel.query.filter_by(cpf=data['cpf']).first()
    if user:
        return True
    return False

def get_all() -> list:
    employees_list: list[EmployeesModel] = EmployeesModel.query.all()
    return [employee.serialize() for employee in employees_list], HTTPStatus.OK

def get_by_id(id) -> EmployeesModel:
    employee: EmployeesModel = EmployeesModel.query.get(id)
    if employee:
        return employee.serialize(), HTTPStatus.OK
    return {}, HTTPStatus.NOT_FOUND

def login() -> dict:
    parser = reqparse.RequestParser()
    
    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args()

    user: EmployeesModel = EmployeesModel.query.filter_by(login=data['login']).first()

    if not user:
        return {
            "error": "User not Found"
        }, HTTPStatus.NOT_FOUND

    if user.check_password(data['password']):
        token = create_access_token(identity=user)
        return {
            "token": token
        }, HTTPStatus.OK
    else:
        return {
            "error": "Invalid password or login information"
        }, HTTPStatus.UNAUTHORIZED

def create_employee() -> EmployeesModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("login", type=str, required=True)
    parser.add_argument("cpf", type=str, required=True)
    parser.add_argument("is_admin", type=bool, required=False)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args(strict=True)

    if data['cpf'] != None and len(data['cpf']) != 11:
        raise("Error")
    
    if get_employee_by_login(data) or check_cpf(data):
        raise DuplicatedKeys

    new_employee: EmployeesModel = EmployeesModel(**data)

    add_commit(new_employee)

    return new_employee.serialize()


def update_employee(id) -> EmployeesModel:
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=False)
    parser.add_argument("login", type=str, required=False)
    parser.add_argument("cpf", type=str, required=False)
    parser.add_argument("is_admin", type=bool, required=False)
    parser.add_argument("password", type=str, required=False)

    employee:EmployeesModel = EmployeesModel.query.get(id)
    if not employee:
        raise("Error")
    
    data = parser.parse_args(strict=True)

    if data['cpf'] != None and len(data['cpf']) != 11:
        return {"error": "CPF must have 11 digits"}, HTTPStatus.BAD_REQUEST

    for key,value in data.items():
        if value != None:
            setattr(employee, key, value)
    
    add_commit(employee)

    return employee.serialize(), HTTPStatus.OK

def delete_employee(id) -> str:
    session = current_app.db.session

    employee = EmployeesModel.query.get(id)

    session.delete(employee)
    session.commit()

    return "", HTTPStatus.NO_CONTENT



