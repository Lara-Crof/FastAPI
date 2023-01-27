from sqlalchemy import MetaData,  Table, Column, Integer, String  
from sqlalchemy.types import  TIMESTAMP, ForeignKey, JSON, 
from datetime import datetime


metadata = MetaData()


role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nulable=False),
    Column('permission', JSON ),
)


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key = True),
    Column("email", String, nullable = False),
    Column('username', String, nullable= False),
    Column("password", String, nullable= False),
    Column("register-at", TIMESTAMP, default=datetime.utcnow),
    Column('role)id', Integer, ForeignKey(role.id)),
)


