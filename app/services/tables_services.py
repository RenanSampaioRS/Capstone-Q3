from app.services.users_services import user_coupon
from flask import request
from sqlalchemy.sql.expression import null
from werkzeug.exceptions import NotFound
from .helpers import add_commit, delete_commit
from flask_restful import reqparse
from app.models.restaurant_table_model import RestaurantTableModel
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from app.models.orders_model import OrdersModel
from app.models.users_model import UsersModel
from app.exc import DuplicatedKeys


def get_all() -> list:
    args = request.args
    response = []

    if "empty" in args and "number" not in args:
        empty = args['empty']
        query = RestaurantTableModel.query.filter_by(empty=empty).all()
        response += query

    if "number" in args and "empty" not in args:
        number = args['number']
        query = RestaurantTableModel.query.filter_by(number=number).all()
        response += query

    if "number" in args and "empty" in args:
        number = args['number']
        empty = args['empty']
        query = RestaurantTableModel.query.filter_by(number=number, empty=empty).all()
        response += query

    if "empty" not in args and "number" not in args:
        query = RestaurantTableModel.query.all()
        response += query
    
    if response == []:
        raise("Error")

    if response[0] == None:
        raise("Error")

    list_optional_atr = []

    for value in response:
        list_optional_atr.append(value.serialize())

    return list_optional_atr



def get_table_by_login(data) -> RestaurantTableModel:
    table: RestaurantTableModel = RestaurantTableModel.query.filter_by(
        login=data["login"]
    ).first()
    return table


def create_table() -> RestaurantTableModel:

    parser = reqparse.RequestParser()

    parser.add_argument("number", type=int, required=True)
    parser.add_argument("seats", type=int, required=True)
    parser.add_argument("empty", type=bool, required=False)
    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args(strict=True)

    if get_table_by_login(data):
        raise DuplicatedKeys

    new_table: RestaurantTableModel = RestaurantTableModel(**data)

    add_commit(new_table)

    return {
        "id": new_table.id,
        "login": new_table.login,
        "number": new_table.number,
        "seats": new_table.seats,
        "empty": new_table.empty,
    }


def login_table():

    parser = reqparse.RequestParser()

    parser.add_argument("login", type=str, required=True)
    parser.add_argument("password", type=str, required=True)

    data = parser.parse_args(strict=True)

    user: RestaurantTableModel = RestaurantTableModel.query.filter_by(
        login=data["login"]
    ).first()

    if not user:
        raise NotFound

    if user.check_password(data["password"]):
        token = create_access_token(identity=user)
        return {"token": token}, HTTPStatus.OK
    else:
        return {
            "error": "Invalid password or login information"
        }, HTTPStatus.UNAUTHORIZED


def delete_table(table_id) -> str:
    found_table = RestaurantTableModel.query.get(table_id)

    if not found_table:
        raise NotFound

    delete_commit(found_table)

    return "", HTTPStatus.NO_CONTENT


def update_table(table_id: int) -> RestaurantTableModel:
    parser = reqparse.RequestParser()

    parser.add_argument("number", type=int, required=False)
    parser.add_argument("seats", type=int, required=False)
    parser.add_argument("total", type=int, required=False)
    parser.add_argument("empty", type=bool, required=False)
    parser.add_argument("password", type=str, required=False)
    parser.add_argument("login", type=str, required=False)

    data = parser.parse_args(strict=True)

    table = RestaurantTableModel.query.get(table_id)

    if not table:
        raise ("Error")

    for key, value in data.items():
        if value != None:
            setattr(table, key, value)

    add_commit(table)
    value_serialize = table.serialize()
    value_serialize["orders_list"] = f"/api/orders?table_id={table.id}"

    return value_serialize, HTTPStatus.OK


def get_by_id(table_id) -> RestaurantTableModel:
    table = RestaurantTableModel.query.get(table_id)

    if table:
        value_serialize = table.serialize()
        value_serialize["orders_list"] = f"/api/orders?table_id={table.id}"
        return value_serialize, HTTPStatus.OK

    return {"status": "table not found!"}, HTTPStatus.NOT_FOUND


def paybill_table(id):
    orders_to_pay = OrdersModel.query.filter_by(table_id=id, cooking=True, ready=True, delivered=True, paid=False).all()

    table = RestaurantTableModel.query.filter_by(id=id).first()

    if not table:
        raise("Error")

    if orders_to_pay != []:    
        if table.user_id != None:    
            user = UsersModel.query.get(table.user_id)         
            coupon = user_coupon(table, user)
            setattr(user, "total", user.total + table.total)
            add_commit(user)
            
        setattr(table, "user_id", None)
        setattr(table, "total", 0)
        setattr(table, "empty", True)
        add_commit(table)

        for order in orders_to_pay:
            setattr(order, "paid", True)
            add_commit(order)
        
        if coupon == null:
            return {"message": "payment completed!"}
        return coupon

    return {"message": "There are no orders to be paid at the moment!"}



    
   

