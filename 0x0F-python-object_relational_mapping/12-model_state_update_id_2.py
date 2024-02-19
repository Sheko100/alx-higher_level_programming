#!/usr/bin/python3
"""Module that updates the name of the state with id = 2 to 'New Mexico'
in 'states' table using SQLAlchemy
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).one_or_none()
    if state:
        state.name = 'New Mexico'
    session.commit()
