#!/usr/bin/python3
"""Module that selects a satte by name
from the 'states' table using SQLAlchemy
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    state_name = argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=state_name).one_or_none()
    if state:
        print(state.id)
    else:
        print('Not found')
