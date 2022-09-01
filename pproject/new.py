from importlib.metadata import metadata


from msilib import schema
from optparse import Values
from sqlalchemy import create_engine
from sqlalchemy.schema import Index
from sqlalchemy.schema import Index


import cx_Oracle
from fastapi import FastAPI
from pydantic import BaseModel
 
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


app=FastAPI()

host='127.0.0.1'
port=1521
sid='xe'
user='system'
password='oracle'

cstr = "oracle+cx_oracle://system:oracle@localhost:1521/xe"
engine =  create_engine(
  cstr
)


metadata_obj = MetaData()
t2= Table('t2', metadata_obj,
Column('id', Integer, primary_key=True),
Column('name', String(30)),


 )

    
metadata_obj.create_all(engine)
conn=engine.connect()