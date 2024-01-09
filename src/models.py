import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique= True)
    password = Column(String(250), nullable=False)
    subscription_date = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    status = Column(String(250))
    species = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    ##character_id = Column(Integer, primary_key=True)
    


class Favoritecharacter(Base):   
   __tablename__ = 'favoritecharacter'
   id = Column(Integer, primary_key=True)
   id_user = Column(Integer, ForeignKey('user.id')) # Marca el id del usuario que selecciona un personaje como favorito
   user = relationship(User)
   id_character = Column(Integer, ForeignKey('character.id')) # Marca el id del personaje que ha sido seleccionado como favorito
   character = relationship(Character)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
