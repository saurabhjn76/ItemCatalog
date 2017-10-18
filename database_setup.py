import os, sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Sports(Base):
    __tablename__ = 'sports'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class SportsPlayer(Base):
    __tablename__ = 'sports_player'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    country = Column(String(200))
    rank = Column(String(8))
    sports_id = Column(Integer, ForeignKey('sports.id'))
    sports = relationship(Sports)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'country': self.country,
            'rank': self.rank,
        }


engine = create_engine('sqlite:///sports.db')


Base.metadata.create_all(engine)