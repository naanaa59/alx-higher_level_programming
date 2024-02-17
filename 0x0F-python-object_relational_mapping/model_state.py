#!/usr/bin/python3
"""
    This script contains the class definition of a State and an instance
    Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


class State(Base):
    """
        This is class State that inherits from Base
    """
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
