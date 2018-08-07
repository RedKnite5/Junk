# sqlalchemy_learning_query.py

from sqlalchemy_learning_dec import Base, Calculation
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sqlalchemy_learning.db')

Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker()

session = DBSession()

result = session.query(Calculation).all()


def show_history(results):
    print("-" * 62)
    for i in results:
        print("|{: <20s}|{: <5s}|{: <6s}|{: <26s}|".format(str(i.query), str(i.answer), str(i.validity), str(i.datetime)))
        print("-" * 62)

show_history(result)
