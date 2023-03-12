from sqlalchemy import create_engine, insert, MetaData, select
from sqlalchemy import Column
from sqlalchemy import Integer

from sqlalchemy import String
from sqlalchemy.orm import declarative_base, sessionmaker

import constant

engine = create_engine(f'sqlite:///{constant.DBNAME}', connect_args={'check_same_thread': False}, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):  # create table "users"
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    name = Column(String(30))


Base.metadata.create_all(engine)


def add_item(message_id, name):
    user = User(message_id=message_id, name=name)
    session.add(user)
    session.commit()


def get_id(name):
    query = select(User.message_id).where(User.name == name)
    result = session.execute(query).fetchone()
    return result[0] if result is not None else None
