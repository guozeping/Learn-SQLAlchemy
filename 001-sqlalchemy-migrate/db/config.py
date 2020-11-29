#!/usr/bin/env  python
# --*--coding:utf-8 --*--
import os
from migrate.versioning import api
basedir = os.path.abspath(os.path.dirname(__file__))

# db settings
DBMS = "mysql"
ADAPTER = "pymysql"
USER = "root"
HOST = "localhost"
PORT = "3306"
DATABASE = "orders"

SQLALCHEMY_DATABASE_URI = DBMS + '+' + ADAPTER + '://' + USER + '@' + HOST + ':' + PORT + '/' + DATABASE
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
SQLALCHEMY_TRACK_MODIFICATIONS = True
