#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DB_URI = 'sqlite:///test.db'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

PER_PAGE = 10
