import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    project configuration domain for api settings, 
    deployment, test and development.
    """
    
    URL_HTTP=os.getenv('URL_HTTP')

    INFURA_HTTP=os.getenv('INFURA_HTTP')
    
    INFURA_WSS=os.getenv('INFURA_WSS')
    