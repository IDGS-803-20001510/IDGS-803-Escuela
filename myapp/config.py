import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY='SUPER_SECRET_KEY'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:1234@localhost:3306/idgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS=False