#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from sqlalchemy import Column
from sqlalchemy import String

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(30))
    password = Column(String(30))
