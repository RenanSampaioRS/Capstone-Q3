from app.services.employees_services import get_by_id
from flask_restful import Resource
from http import HTTPStatus
from app.services.users_services import get_all, delete_user, update_user, create_user
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_jwt_extended import jwt_required


class UsersResource(Resource):
    @jwt_required()
    def get(self):
        try:
            return get_all(), HTTPStatus.OK      
        except TypeError as _:
            return {"error": "Invalid parameters!"}, HTTPStatus.NOT_FOUND

    def post(self):
        try:
            return create_user(), HTTPStatus.CREATED
        except DataError as _:
            return {"error": "Invalid CPF"}, HTTPStatus.BAD_REQUEST
        except IntegrityError as _:
            return {"error": "Cpf already exists!"}, HTTPStatus.NOT_FOUND
        except TypeError as _:
            return {"error": "Wrong lenght of parameters!"}, HTTPStatus.BAD_REQUEST
        


class UserIdResource(Resource):
    @jwt_required()
    def get(self, user_id: int):
        return get_by_id(user_id)

    @jwt_required()
    def patch(self, user_id: int):
        try:
            return update_user(user_id), HTTPStatus.OK
        except TypeError as _:
            return {"error": "User not found"}, HTTPStatus.NOT_FOUND
        except DataError as _:
            return {"error": "Invalid CPF"}, HTTPStatus.UNPROCESSABLE_ENTITY

    @jwt_required()
    def delete(self, user_id: int):
        try:
            return delete_user(user_id), HTTPStatus.NO_CONTENT
        except TypeError as _:
            return {"error": "User not found"}, HTTPStatus.NOT_FOUND
        except UnmappedInstanceError as _:
            return {"error": "User not found"}, HTTPStatus.NOT_FOUND
