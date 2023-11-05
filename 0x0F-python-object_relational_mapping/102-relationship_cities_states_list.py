#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa."""

import sys
from relationship_city import Base, City, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print(f'{city.id}: {city.name} -> {state.name}')

    session.close()
