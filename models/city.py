#!/usr/bin/python3

"""
A module that defines the ORM class for City table
"""
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship(
            'Place', backref='cities', cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
