#!/usr/bin/python3
"""
    This script prints all City objects from db hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
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

    all_obj = session.query(State, City).filter(State.id == City.
                                                state_id).all()

    for state, city in all_obj:
        print(f"{state.name}: ({city.id}) {city.name}")
