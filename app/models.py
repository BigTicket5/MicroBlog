'''
Created on 2014-5-23

@author: KEVIN
'''
from sqlalchemy import Column, Integer, String,SmallInteger
from app.database import Base
ROLE_USER = 0
ROLE_ADMIN = 1
class User(Base):
    __tablename__='User'
    id = Column(Integer, primary_key = True)
    nickname = Column(String(64), unique=True,index = True)
    email = Column(String(120), unique=True, index = True)
    role = Column(SmallInteger,default =  ROLE_USER)
    about_me = Column(String(140))
    def __init__(self, nickname=None, email= None , role = ROLE_USER ):
        self.nickname = nickname
        self.email = email
        self.role = role
    def __repr__(self):
        return '<User %r>' % (self.nickname)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return True
    def get_id(self):
        return (self.id)
  
    


    
    
    
