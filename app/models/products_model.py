from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import Float, String
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class ProductsModel(db.Model):
    id: int
    name: str
    price: int
    calories: int
    section: str
    is_veggie: bool

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String(150), nullable=False)
    price = Column(Float, nullable=False)
    calories = Column(Float)
    section = Column(String(150))
    is_veggie = Column(Boolean, default=False)

    def serialize(self):
        return {"id": self.id, "price": self.price, "name": self.name, "calories": self.calories, "section": self.section, "is_veggie": self.is_veggie}
    
