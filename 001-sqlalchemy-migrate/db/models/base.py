#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

Base = declarative_base()

class BaseModel(Base):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean)
    status = Column(Boolean)
    is_active = Column(Boolean)