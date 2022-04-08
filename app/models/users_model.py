from app.configs.database import db
from sqlalchemy import Column, Integer, String, Float
from dataclasses import dataclass


@dataclass
class UsersModel(db.Model):
    id: int
    cpf: str
    name: str
    total: float

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), nullable=False, unique=True)
    name = Column(String(150), nullable=False)
    total = Column(Float, default=0)

    def serialize(self):
        return {"id": self.id, "name": self.name, "cpf": self.cpf, "total": self.total}
