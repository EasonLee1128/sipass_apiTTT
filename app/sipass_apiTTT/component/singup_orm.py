
#from pandas import DataFrame
#from pymongo import MongoClient
from sqlalchemy import Column, Integer, String, create_engine , String, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import hashlib

Base = declarative_base()
engine_url ='mysql+pymysql://root:111111@127.0.0.1:3306/dataDB'
engine = create_engine(engine_url, echo=True)

class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55))
    time = Column(DATETIME)
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    username = Column(String(55))
    password = Column(String(55))

class Signup(Base):
    __tablename__ = 'signup'
    id = Column(Integer, primary_key=True)
    
    username = Column(String(55))
    #password = Column(String(55))   
    hash_password = Column(String(55))
    create_time = Column(DATETIME) 
    update_time = Column(DATETIME) 
    enable_state = Column(String(1))
   
    
def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)

def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def hash_PWD(password):
    hashobj = hashlib.sha256()
    hashobj.update(password.encode('utf-8'))
    return  hashobj.hexdigest()[:32]            #回傳32位數