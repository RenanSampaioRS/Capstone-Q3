from http import HTTPStatus
from app.exc import DuplicatedKeys
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.services.employees_services import (
    get_all,
    get_by_id,
    update_employee,
    create_employee,
    delete_employee,
    login,
)


class EmployeesResource(Resource):
    @jwt_required()
    def get(self):
        return get_all()
    
    def post(self):
        try:
            return create_employee()
        except DuplicatedKeys:
            return {"error": "Duplicated information!"}, HTTPStatus.BAD_REQUEST
        except IntegrityError:
            return {"error": "Wrong lenght of parameters!"}, HTTPStatus.BAD_REQUEST
        except TypeError as _:
            return {"error": "CPF must have 11 digits!"}, HTTPStatus.BAD_REQUEST


class EmployeeIDResource(Resource):
    @jwt_required()
    def get(self, employee_id: int):
        return get_by_id(employee_id)

    @jwt_required()
    def patch(self, employee_id: int):
        try:
            return update_employee(employee_id)
        except DataError:
            return {"error": "Wrong lenght of parameters!"}, HTTPStatus.BAD_REQUEST
        except IntegrityError:
            return {"error": "Cpf already exists!"}, HTTPStatus.BAD_REQUEST
        except TypeError as e:
            return {"error": "Employee doesn't exist!"}, HTTPStatus.BAD_REQUEST

    @jwt_required()
    def delete(self, employee_id: int):
        try:
            return delete_employee(employee_id)
        except UnmappedInstanceError as e:
            return {"error": "Employee doesn't exist!"}, HTTPStatus.BAD_REQUEST


class EmployeeLoginResource(Resource):
    def post(self):
        try:
            return login()
        except IntegrityError:
            return {"error": "Wrong lenght of parameters"}, HTTPStatus.BAD_REQUEST
