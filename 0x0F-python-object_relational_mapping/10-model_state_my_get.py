#!/usr/bin/python3
''' Prints the State object with the [name] passed as argument '''
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
             'mysql+mysqldb://{}:{}@localhost/{}'.format(
              sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    search = sys.argv[4]

    state = session.query(State).filter(text("name='{}'".format(search)))
    state = state.first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
