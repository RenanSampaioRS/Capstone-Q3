from app.services.products_orders_services import delete_product_order_by_order, relate_product_order, total_table
from app.models.orders_model import OrdersModel
from app.services.helpers import add_commit, delete_commit
from http import HTTPStatus
from flask import request
from flask_restful import reqparse


def create_order():    
    parser = reqparse.RequestParser()
    
    parser.add_argument("table_id",type = int, required=True)
    parser.add_argument("date", type = str, required=True)
    parser.add_argument("estimated_arrival", type = str)
    parser.add_argument("cooking", type = bool)
    parser.add_argument("ready", type = bool)
    parser.add_argument("delivered", type = bool)
    parser.add_argument("paid", type = bool)
    parser.add_argument("products", type = list, location = "json")

    args = parser.parse_args(strict=True)

    products = args.pop('products')

    order: OrdersModel = OrdersModel(**args)
    
    add_commit(order)
    
    total_table(products, order.table_id)

    for i in products: 
        relate_product_order(order.id, i)

    return order.serialize()

def get_current_orders(table_id: int, cooking: bool, ready: bool, delivered: bool) -> dict:

    order = OrdersModel
    query = order.query.filter(order.table_id == table_id,order.cooking == cooking,order.ready == ready,order.delivered == delivered).all()

    return query, HTTPStatus.OK

def get_orders(): ## ok
    args = request.args
    response = []

    if "table_id" in args and "ready" not in args and "paid" not in args:
        table_id = args["table_id"]
        query = OrdersModel.query.filter_by(table_id=table_id).all()
        response += query

    if "table_id" not in args and "ready" in args and "paid" not in args:
        ready = args["ready"]
        query = OrdersModel.query.filter_by(ready=ready).all()
        response += query
    
    if "table_id" not in args and "ready" not in args and "paid" in args:
        paid = args["paid"]
        query = OrdersModel.query.filter_by(paid=paid).all()
        response += query

    if "table_id" in args and "ready" not in args and "paid" in args:
        table_id = args["table_id"]
        paid = args["paid"]
        query = OrdersModel.query.filter_by(table_id=table_id, paid=paid).all()
        response += query
    
    if "table_id" in args and "ready" in args and "paid" not in args:
        table_id = args["table_id"]
        ready = args["ready"]
        query = OrdersModel.query.filter_by(table_id=table_id, ready=ready).all()
        response += query
    
    if "table_id" not in args and "ready" in args and "paid" in args:
        ready = args["ready"]
        paid = args["paid"]
        query = OrdersModel.query.filter_by(ready=ready, paid=paid).all()
        response += query
    
    if "table_id" in args and "ready" in args and "paid" in args:
        table_id = args["table_id"]
        ready = args["ready"]
        paid = args["paid"]
        query = OrdersModel.query.filter_by(table_id=table_id,ready=ready, paid=paid).all()
        response += query
    
    if "table_id" not in args and "ready" not in args and "paid" not in args:
        query = OrdersModel.query.all()
        response += query
    

    if response != []:
        list_optional_atr = []

        for value in response:
            list_optional_atr.append(value.serialize())

        return list_optional_atr
    else:
        return []


def get_order(order_id: int) -> dict: ##ok
    order = OrdersModel

    query = order.query.get(order_id)

    if query:
        return query.serialize(), HTTPStatus.OK
    
    return {"error":"Order not found"}, HTTPStatus.NOT_FOUND

def remove_order(id:int) -> None: ##ok

    order = OrdersModel
    query = order.query.get(id)

    delete_product_order_by_order(query.id)

    delete_commit(query)

    return ""


def update_order(id: int) -> dict:

    parser = reqparse.RequestParser()
    
    parser.add_argument("table_id",type = int)
    parser.add_argument("date", type = str)
    parser.add_argument("estimated_arrival", type = str)
    parser.add_argument("cooking", type = bool)
    parser.add_argument("ready", type = bool)
    parser.add_argument("delivered", type = bool)
    parser.add_argument("paid", type = bool)

    data = parser.parse_args(strict=True)

    order = OrdersModel
    
    query = order.query.get(id)

    if not query:
        raise("Error")

    for key, value in data.items():
        if value != None:
            setattr(query, key, value)

    add_commit(query)
    return {
        "id":query.id,
        "table_id":query.table_id,
        "date":str(query.date),
        "estimated_arrival":str(query.estimated_arrival),
        "cooking":query.cooking,
        "ready":query.ready,
        "delivered":query.delivered,
        "paid":query.paid,
    }
