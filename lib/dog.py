from models import Dog
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True)
    name =  Column(String)
    breed = Column(String)
    
    #function to create a sqlite database
def create_table(base, engine):
    base.metadata.create_all(engine) #creates the "dogs" table
    
#func to save Dog instance to the database
def save(session, dog):
    session.add(dog)
    session.commit()
#func to 
def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
  return  session.query(Dog).filter_by(name=name).first()
def find_by_id(session, id):
   return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
   return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()