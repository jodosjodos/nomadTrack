from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from app.database import Base

# Many-to-Many relationship table for Travel and Checklist
travel_checklist_association = Table(
    'travel_checklist',
    Base.metadata,
    Column('travel_id', Integer, ForeignKey('travels.id')),
    Column('checklist_id', Integer, ForeignKey('checklists.id'))
)

class User(Base):  # Simplified User model
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, unique=False, index=True)

class Checklist(Base):
    __tablename__ = 'checklists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

class Travel(Base):
    __tablename__ = 'travels'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100))
    city = Column(String(100))
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    checklists = relationship(
        "Checklist", secondary=travel_checklist_association, back_populates="travels"
    )

Checklist.travels = relationship(
    "Travel", secondary=travel_checklist_association, back_populates="checklists"
)

class Checking(Base):
    __tablename__ = 'checkings'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    visit = Column(String(100), default="Visited On")
    travel_id = Column(Integer, ForeignKey('travels.id'))
    travel = relationship("Travel")
