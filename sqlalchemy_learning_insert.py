# sqlalchemy_learning_insert.py

from ReCalc_objects import NonRepeatingList
import pickle
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_learning_dec import Base, Calculation

engine = create_engine('sqlite:///sqlalchemy_learning.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


pathname = "C:\\Users\\Max\\Documents\\Python\\ReCalc\\ReCalc_info.txt"
with open(pathname, "rb") as file:
	info = pickle.load(file)
	history = info["history"]
	
	for i in history:
		query = Calculation(query = i)
		session.add(query)
		session.commit()
