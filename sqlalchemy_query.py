# sqlalchemy_query.py

from sqlalchemy_declarative import Person, Base, Address
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
print(session.query(Person).all())

# Return the first Person from all Persons in the database
person = session.query(Person).first()
print(person.name)

print(session.query(Address).filter(Address.person == person).all())
