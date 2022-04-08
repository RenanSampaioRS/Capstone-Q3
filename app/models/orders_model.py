from app.services.products_services import get_product_by_order_id
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Integer, Column, Boolean, DateTime
from dataclasses import dataclass


@dataclass
class OrdersModel(db.Model):
    table_id: int
    date: str
    estimated_arrival: str
    cooking: bool
    ready: bool
    delivered: bool
    paid: bool

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    table_id = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    estimated_arrival = Column(DateTime)
    cooking = Column(Boolean, default=False)
    ready = Column(Boolean, default=False)
    delivered = Column(Boolean, default=False)
    paid = Column(Boolean, default=False)

    table_id = Column(Integer, ForeignKey("restaurant_tables.id"))
    table = relationship("RestaurantTableModel", backref="restaurant_tables")

    def serialize(self):
        return {
                "id":self.id,
                "table_id":self.table_id,
                "date":str(self.date),
                "estimated_arrival":str(self.estimated_arrival),
                "cooking":self.cooking,
                "ready":self.ready,
                "delivered":self.delivered,
                "paid":self.paid,
                "products": get_product_by_order_id(self.id)
        }

