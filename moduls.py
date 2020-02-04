import datetime
import math
from sqlalchemy import (Column, VARCHAR, String, 
                        Integer, Text, DateTime, 
                        Boolean, ForeignKey, create_engine)
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///app.db', echo = True)

Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String(20), unique = True, nullable = True)
    password = Column(String(30), nullable = True)
    email = Column(String(50),unique = True, nullable = True)
    registred_on = Column(DateTime, default = datetime.date.today())

    def __str__(self):
        return '\n'.join([self.id, 
                            self.name, 
                            self.password, 
                            self.email, 
                            self.registred_on])


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = True)
    title = Column(String(20), nullable = True)
    description = Column(String(30), nullable = True)
    created_on = Column(DateTime, default = datetime.date.today())
    finish_up = Column(DateTime)
    status = Column(Boolean, default = 0)

    def __str__(self):
        return '\n'.join([self.id, 
                            self.user_id, 
                            self.title, 
                            self.description, 
                            self.created_on,
                            self.finish_up,
                            self.status])


Base.metadata.create_all()

def add_user(name, email, password):
    engine = create_engine('sqlite:///app.db', echo = True)
    session = Session(bind = engine)
    session.add(User(name = name, email = email, password = password))
    session.commit()
    session.close()

def check_user(email, password):
    engine = create_engine('sqlite:///app.db', echo = True)
    session = Session(bind = engine)
    user = session.query(User).filter_by(email = email, password = password).first()
    session.close()
    return user


def add_task(tatle, details, deadline_date):
    engine = create_engine('sqlite:///app.bd', echo = True)
    db_session = Session(bind = engine)
    user_task = db_session.query(User).filter_by(name=user).first().task
    deadline_date = datetime.date.fromisoformat(deadline_date)

    db_session.commit()
    db_session.close()

def get_user_task():
    engine = create_engine('sqlite:///app.db', echo=True)
    db_session = Session(bind=engine)
    db_user = db_session.query(User).filter_by(name=name).first()
    user_tasks = db_user.tasks
    db_session.close()
    return db_user.tasks  














