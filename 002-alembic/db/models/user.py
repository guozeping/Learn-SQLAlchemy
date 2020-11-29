#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from .base import BaseModel
from sqlalchemy import Column
from sqlalchemy import String

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(30))
    password = Column(String(30))



