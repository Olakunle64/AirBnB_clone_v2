#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
    # state_id = ""
    # name = ""
