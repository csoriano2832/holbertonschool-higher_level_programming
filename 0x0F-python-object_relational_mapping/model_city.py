#!/usr/bin/python3
''' This module defines a class '''
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    ''' This class defines a City object '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
