from app.models.restaurant_table_model import RestaurantTableModel
from app.models.orders_model import OrdersModel
from app.models.products_model import ProductsModel
from app.models.products_orders_model import ProductsOrdersModel
from app.services.helpers import add_commit, delete_commit


def relate_product_order(order_id, product_id): 
    
    order = OrdersModel.query.get(order_id)
    product = ProductsModel.query.get(product_id)

    if order and product:
        product_order = ProductsOrdersModel(product_id=product.id, order_id=order.id)
    
        add_commit(product_order)
    
def delete_product_order_by_order(order_id):

    query = ProductsOrdersModel.query.filter_by(order_id=order_id).all()

    for elem in query: 
        delete_commit(elem)
    
def total_table(products, table_id):

    query = RestaurantTableModel.query.get(table_id)

    for product in products:
        product_filtered = ProductsModel.query.get(product)
        setattr(query, "total", query.total + product_filtered.price)
        add_commit(query)
    






