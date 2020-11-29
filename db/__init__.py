#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from sqlalchemy.engine import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/orders')

metadata = MetaData(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)


