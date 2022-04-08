from http import HTTPStatus
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.functions import user
from app.models.users_model import UsersModel
from flask import request
from flask_restful import reqparse
from app.services.helpers import add_commit, delete_commit

def get_all():

    args = request.args
    response = []

    if "cpf" in args and "name" not in args:
        cpf = args['cpf']
        query = UsersModel.query.filter_by(cpf=cpf).all()
        response += query

    if "name" in args and "cpf" not in args:
        name = args['name']
        query = UsersModel.query.filter_by(name=name).all()
        response += query

    if "name" in args and "cpf" in args:
        name = args['name']
        cpf = args['cpf']
        query = UsersModel.query.filter_by(name=name, cpf=cpf).all()
        response += query

    if "cpf" not in args and "name" not in args:
        query = UsersModel.query.all()
        response += query
    

    if response != []:
        list_optional_atr = []

        for value in response:
            list_optional_atr.append(value.serialize())

        return list_optional_atr
    else:
        return []

def get_by_id(user_id) -> UsersModel:
    user = UsersModel.query.get(user_id)

    if user:
        value_serialize = user.serialize()
        return value_serialize, HTTPStatus.OK
    return {"error": "User not found!"}, HTTPStatus.NOT_FOUND


def get_user(user_cpf: str) -> dict:
    user = UsersModel()
    query = user.query.filter_by(cpf=user_cpf).first()
    return query.serialize()


def create_user():
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True)
    parser.add_argument("cpf", type=str, required=True)

    data = parser.parse_args(strict=True)

    if data['cpf'] != None and len(data['cpf']) != 11:
        raise("Error")

    new_user = UsersModel(**data)
    add_commit(new_user)
    return new_user.serialize()


def update_user(id: int) -> dict:
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("cpf", type=str)
    parser.add_argument("total", type=float)

    data = parser.parse_args(strict=True)

    user = UsersModel()

    query = user.query.get(id)

    if not query:
        raise("Error")

    for key, value in data.items():
        if value != None:
            setattr(query, key, value)

    add_commit(query)
    return query.serialize()


def delete_user(id: int):
    query = UsersModel.query.get(id)

    delete_commit(query)

    return "", HTTPStatus.NO_CONTENT

def user_coupon(table, user):
    if int(user.total) >= 400:
        old_total = table.total
        new_total = table.total - table.total*(0.2)
        setattr(table, "total", new_total)
        setattr(user, "total", 0)
        add_commit(table)
        add_commit(user)
        return {"Total without discount": old_total, "Total with discount": table.total}
    return null
    