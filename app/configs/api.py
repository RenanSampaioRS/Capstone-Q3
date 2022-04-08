from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.views.employees_view import EmployeeIDResource, EmployeesResource, EmployeeLoginResource

    api.add_resource(EmployeesResource, "/api/employees", endpoint="EMPLOYEES")
    api.add_resource(EmployeeIDResource, "/api/employees/<int:employee_id>", endpoint="EMPLOYEE_ID")
    api.add_resource(EmployeeLoginResource, "/api/employees/login", endpoint="EMPLOYEE_LOGIN")

    from app.views.orders_views import OrdersResource, OrderIDResource

    api.add_resource(OrdersResource, "/api/orders", endpoint="ORDERS")
    api.add_resource(OrderIDResource, "/api/orders/<int:order_id>", endpoint="ORDER_ID")

    from app.views.products_view import ProductsResource, ProductIDResource

    api.add_resource(ProductsResource, "/api/products", endpoint="PRODUCTS")
    api.add_resource(
        ProductIDResource, "/api/products/<int:product_id>", endpoint="PRODUCTS_ID"
    )

    from app.views.users_view import UsersResource, UserIdResource

    api.add_resource(UsersResource, "/api/users", endpoint="USERS")
    api.add_resource(UserIdResource, "/api/users/<int:user_id>", endpoint="USERS_ID")

    from app.views.tables_view import (
        TablesResource,
        TableIdResource,
        TableLoginResource,
        TableCloseOrders
    )

    api.add_resource(TablesResource, "/api/tables", endpoint="TABLES")
    api.add_resource(TableLoginResource, "/api/tables/login", endpoint="TABLE_LOGIN")
    api.add_resource(TableIdResource, "/api/tables/<int:id>", endpoint="TABLES_ID")
    api.add_resource(TableCloseOrders, "/api/tables/paybill/<int:id>", endpoint="TABLES_CLOSE")
