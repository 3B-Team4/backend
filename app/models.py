# Database tables

from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import ARRAY

import logging
logger = logging.getLogger(__name__)

userRooms = Table('userRooms', Base.metadata,
                  Column('id', Integer, primary_key=True),
                  Column('userId', Integer, ForeignKey('users.id')),
                  Column('roomId', Integer, ForeignKey('ChatRooms.id')))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(100), unique=False, nullable=False)
    userType = Column(Boolean, unique=False, nullable=False)
    rooms = relationship("ChatRooms", secondary=userRooms,
                         back_populates='users')
    messages = relationship("Messages")

    def __init__(self, name=None, email=None, password=None, userType=None):
        self.name = name
        self.email = email
        self.password = password
        self.userType = userType

    def __repr__(self):
        return '<User %r>' % (self.name)



class CovidCases(Base):
    __tablename__ = 'Covid Cases'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(150), nullable=False)
    mobile = Column(Integer, unique=False, nullable=False)
    lat = Column(Float, unique=False, nullable=False)
    lng = Column(Float, unique=False, nullable=False)

    def __init__(self, first_name=None, last_name=None, mobile=None, lat=None, lng=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.lat = lat
        self.lng = lng


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, unique=True, nullable=False)


class ChatRooms(Base):
    __tablename__ = 'ChatRooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    roomName = Column(String(100), nullable=False)
    messages = relationship(
        'Messages', backref='ChatRooms', passive_deletes=True)
    users = relationship('User', secondary=userRooms, back_populates='rooms')


class Messages(Base):
    __tablename__ = 'Messages'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
    roomId = Column(Integer, ForeignKey(
        'ChatRooms.id', ondelete='CASCADE'), nullable=False)
    time = Column(Integer, nullable=False)
    message = Column(String())
    removed = Column(Boolean, nullable=False)
    edited = Column(Boolean, nullable=False)

    def __repr__(self):
        return '<Message %r>' % (self.message)

