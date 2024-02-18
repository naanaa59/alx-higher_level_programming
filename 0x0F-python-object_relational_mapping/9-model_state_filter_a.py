#!/usr/bin/python3
"""
    This script lists all State objects containg a from the database
    hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, db)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print(f"{state.id}: {state.name}")
