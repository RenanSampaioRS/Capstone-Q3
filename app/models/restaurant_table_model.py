from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, Integer, Boolean, String, Float
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass


@dataclass
class RestaurantTableModel(db.Model):
    id: int
    seats: int
    number: int
    total: float
    login: str
    empty: bool
    user_id: int

    __tablename__ = "restaurant_tables"

    id = Column(Integer, primary_key=True)

    seats = Column(Integer, default=0)
    number = Column(Integer, nullable=False, unique=True)
    total = Column(Float, default=0)
    password_hash = Column(String, nullable=False)
    empty = Column(Boolean, default=True)
    login = Column(String(150), nullable=False, unique=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UsersModel", backref="tables")

    orders = relationship("OrdersModel", backref="order")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    def serialize(self):
        return {
            "id": self.id,
            "login": self.login,
            "number": self.number,
            "seats": self.seats,
            "user_id": self.user_id,
            "total": self.total,
            "empty": self.empty,
        }
