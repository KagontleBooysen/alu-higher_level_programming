#!/usr/bin/python3
""" change name of state with id 2 """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Sessionmaker = sessionmaker(bind=engine)
    session = Session()
    state = State(name="Texas")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
