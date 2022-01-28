import os 

class Config:
    """
    project configuration domain for api settings, 
    deployment, test and development.
    """
    
    ACCOUNT=os.environ.get('ACCOUNT')
    
    SECRET = os.environ.get('SECRET')
