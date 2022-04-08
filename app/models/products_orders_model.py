from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey
from dataclasses import dataclass


@dataclass
class ProductsOrdersModel(db.Model):
    id: int
    product_id: int
    order_id: int

    __tablename__ = "products_orders"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)