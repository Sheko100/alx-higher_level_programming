#!/usr/bin/python3
"""Module that defines the State class as a SQLAlchemy table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """Class that defines the State class
    """

    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True,
                autoincrement="auto", nullable=False)
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', back_populates='state')
