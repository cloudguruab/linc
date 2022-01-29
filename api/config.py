import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    project configuration domain for api settings, 
    deployment, test and development.
    """
    
    ACCOUNT=os.getenv('ACCOUNT')
    
    SECRET=os.getenv('SECRET')

    URL_HTTP=os.getenv('URL_HTTP')

    URL_WSS=None 