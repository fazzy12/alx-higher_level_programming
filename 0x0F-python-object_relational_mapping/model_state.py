#!/usr/bin/python3
"""
This module defines a State class and creates a corresponding SQL table.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class represents the "states" table in the database.

    Attributes:
        id (int): An auto-generated, unique integer
        representing the primary key.

        name (str): A string with a maximum of 128
        characters representing the state name.

    Args:
        Base: The base class for SQLAlchemy models.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the "states" table in the database
    Base.metadata.create_all(engine)
