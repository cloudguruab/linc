import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    project configuration domain for api settings, 
    deployment, test and development.
    """
    
    URL_HTTP=os.getenv('URL_HTTP')

    INFURA_HTTP=os.getenv('WEB3_INFURA_HTTP')
    
    INFURA_WSS=os.getenv('WEB3_INFURA_WSS')
    
    DEMO_ACCT=os.getenv('DEMO_ACCT')
    
    SECRET=os.getenv('SECRET')