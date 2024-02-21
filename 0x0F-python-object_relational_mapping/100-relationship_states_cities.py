#!/usr/bin/python3
"""Module that creates state: 'California' linked to city: 'San Francisco'
using SQLAlchemy
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='California')
    session.add(state)
    session.commit()

    city = City(name='San Francisco', state_id=state.id)
    session.add(city)
    session.commit()

    print('hello')
    session.close()
