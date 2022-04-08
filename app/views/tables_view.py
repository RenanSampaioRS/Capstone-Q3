from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError, DataError
from werkzeug.exceptions import NotFound
from app.exc import DuplicatedKeys
from app.services.tables_services import (
    get_all,
    create_table,
    get_by_id,
    delete_table,
    login_table,
    paybill_table,
    update_table,
)


class TablesResource(Resource):
    @jwt_required()
    def get(self):
        try:
            return get_all()
        except DataError:
            return {"error": "Invalid parameter value"}, HTTPStatus.NOT_FOUND
        except TypeError:
            return {"error": "Invalid parameter value"}, HTTPStatus.NOT_FOUND

    @jwt_required()
    def post(self):
        try:
            return create_table()
        except DuplicatedKeys:
            return {"error": "Duplicated information"}, HTTPStatus.BAD_REQUEST
        except IntegrityError:
            return {"error": "Wrong lenght of parameters"}, HTTPStatus.BAD_REQUEST


class TableIdResource(Resource):
    @jwt_required()
    def get(self, id: int):
        return get_by_id(id)

    @jwt_required()
    def delete(self, id: int):
        try:
            return delete_table(id)
        except NotFound as _:
            return {"error": "table not found"}, HTTPStatus.NOT_FOUND

    @jwt_required()
    def patch(self, id: int):
        try:
            return update_table(id)
        except TypeError as _:
            return {"error": "Invalid id"}, HTTPStatus.BAD_REQUEST
        except IntegrityError as _:
            return {"error": "Number table already exists"}, HTTPStatus.BAD_REQUEST


class TableLoginResource(Resource):
    def post(self):
        try:
            return login_table()
        except NotFound as _:
            return {"error": "User not Found"}, HTTPStatus.NOT_FOUND

class TableCloseOrders(Resource):
    def patch(self, id: int):
        try:
            return paybill_table(id)
        except TypeError as _:
            return {"error": "Invalid id"}, HTTPStatus.BAD_REQUEST
