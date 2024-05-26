import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ferremas_user:password@localhost:3306/ferremas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
