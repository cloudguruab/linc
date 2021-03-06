from web3 import Web3
from ..dev.types import GlobalProviderType
from ..dev.exceptions import HttpProviderError, SocketProviderError
from ..config import Config

class LocalProvider:
    """
    Local node provider using strictly http based connections. 
    """
    
    def __init__(self):
        self.url_http: GlobalProviderType.addy = Config.URL_HTTP
    
    def connect(self):
        try:
            w3 = Web3(Web3.HTTPProvider(self.url_http))
        except:            
            raise HttpProviderError
        
        return w3

class HostedProvider:
    """
    Hosted node provider using http and socket based connections.
    """
    
    def __init__(self):
        self.url_http: GlobalProviderType.addy = Config.INFURA_HTTP
        self.url_wss: GlobalProviderType.addy = Config.INFURA_WSS
        
    def connect_http(self):
        try:
            w3 = Web3(Web3.HTTPProvider(self.url_http))
        except:
            raise HttpProviderError
        
        return w3
    
    def connect_socket(self):
        try:
            w3 = Web3(Web3.WebsocketProvider(self.url_wss))
        except: 
            raise SocketProviderError
        
        return w3
