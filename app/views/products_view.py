from os import EX_CANTCREAT
from flask_restful import Resource
from http import HTTPStatus
from sqlalchemy.exc import DataError
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_jwt_extended import jwt_required
from app.services.products_services import (
    get_all,
    get_by_id,
    update_product,
    create_product,
    delete_product,
)


class ProductsResource(Resource):
    @jwt_required()
    def get(self):
        try:
            return get_all(), HTTPStatus.OK
        except DataError as _:
            return {"error": "Invalid parameter value!"}, HTTPStatus.NOT_FOUND

    @jwt_required()
    def post(self):
        return create_product(), HTTPStatus.CREATED


class ProductIDResource(Resource):
    @jwt_required()
    def get(self, product_id: int):
        return get_by_id(product_id)

    @jwt_required()
    def patch(self, product_id: int):
        try:
            return update_product(product_id)
        except TypeError as _:
            return {"error":"Product doesn't exists"}, HTTPStatus.NOT_FOUND

     
    @jwt_required()
    def delete(self, product_id: int):
        try:
            return delete_product(product_id)

        except UnmappedInstanceError as _:
            return {"error": "Product doesn't exists"}, HTTPStatus.NOT_FOUND
        except TypeError as _:
            return {"error": "Product doesn't exists"}, HTTPStatus.NOT_FOUND
