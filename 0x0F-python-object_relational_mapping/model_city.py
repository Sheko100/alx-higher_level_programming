#!/usr/bin/python3
"""Module that defines the City class as a SQLAlchemy table
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """Class that defines the City class
    """

    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True,
                autoincrement="auto", nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column(
            "state_id",
            Integer,
            ForeignKey('states.id'),
            nullable=False)
