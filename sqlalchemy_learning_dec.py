# sqlalchemy_learning_dec.py

import os
import sys
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Calculation(Base):
    __tablename__ = "calculation"

    id = Column(Integer, primary_key = True)
    query = Column(String(250), nullable = False)
    answer = Column(String(250))
    datetime = Column(DateTime, default = datetime.utcnow)
    validity = Column(String(250))

engine = create_engine('sqlite:///sqlalchemy_learning.db')

Base.metadata.create_all(engine)
