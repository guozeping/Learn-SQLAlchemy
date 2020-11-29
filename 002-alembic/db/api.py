#!/usr/bin/env  python
# --*--coding:utf-8 --*--
from db.models.user import User
from db.models.base import session


user = User(username="gzp",password='1234')
session.add(user)
session.commit()
session.close()
