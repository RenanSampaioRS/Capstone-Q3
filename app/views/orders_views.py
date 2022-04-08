from http import HTTPStatus
from flask_restful import Resource
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import DataError, IntegrityError
from app.services.orders_services import create_order, get_orders, get_order, remove_order,update_order
from flask_jwt_extended import jwt_required


class OrdersResource(Resource):
    @jwt_required()
    def post(self):
        try:
            return create_order(),HTTPStatus.CREATED
        except IntegrityError as _:
            return {"error": "Table_Id doesn't exist"}, HTTPStatus.BAD_REQUEST
        except DataError as _:
            return {"error": "Invalid parameter value!"}, HTTPStatus.BAD_REQUEST
    @jwt_required()
    def get(self):      
        try:
            return get_orders(),HTTPStatus.OK
        except DataError as _:
            return {"error": "Invalid parameter value!"}, HTTPStatus.NOT_FOUND
        except TypeError as _:
            return {"error": "Invalid parameters!"}, HTTPStatus.NOT_FOUND


class OrderIDResource(Resource):
    @jwt_required()
    def get(self, order_id: int):
        return get_order(order_id)
        
    @jwt_required()
    def delete(self, order_id: int):
        try:
            return remove_order(order_id), HTTPStatus.NO_CONTENT

        except UnmappedInstanceError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.BAD_REQUEST

        except AttributeError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.BAD_REQUEST
    
    @jwt_required()
    def patch(self, order_id: int):
        try:
            return update_order(order_id), HTTPStatus.CREATED
        
        except UnmappedInstanceError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.BAD_REQUEST

        except TypeError as _:
            return {"error":"Order doesn't exists"}, HTTPStatus.NOT_FOUND
