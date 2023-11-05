#!/usr/bin/python3
""" Creates a State and City from the database hbtn_0e_100_usa """

from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
