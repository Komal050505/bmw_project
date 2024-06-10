from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BMW_Vehicles(Base):
    __tablename__ = "bmw_vehicles"

    id = Column("vehicle_id", Integer, primary_key=True)
    price = Column("price", Integer)
    model = Column("model", String(50))
    year = Column("year", Integer)
    color = Column("color", String(50))

