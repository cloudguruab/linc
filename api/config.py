import os 

class Config:
    """
    project configuration domain for api settings, 
    deployment, test and development.
    """
    
    ENV = None
    SECRET = None
    DB_URSER = None
    DB_PASS = None
    DB_PORT = None
    DB_HOST = None