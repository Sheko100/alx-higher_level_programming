#!/usr/bin/python3
"""Module that selects all rows contains 'a' letter
from the 'states' table using SQLAlchemy
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

    states = session.query(State).filter(
            State.name.contains('a')).order_by(State.id)
    for state in states:
        if state:
            print('{}: {}'.format(state.id, state.name))
        else:
            print('Nothing')
