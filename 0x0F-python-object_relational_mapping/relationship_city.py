#!/usr/bin/python3
"""
    This script contains the class definition of a class City
    This script contains the class definition of a class City
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
        This is class City that inherits from Base from model_state
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship('State', back_populates='cities')
