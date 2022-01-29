from web3 import Web3
from ..dev.providerTypes import GlobalProviderType
from ..dev.exceptions import HttpProviderError, SocketProviderError
from ..config import Config

class Provider:
    """
    Support for web based connections, and integrations for remote node providers. 
    """
    
    def __init__(self):
        self.url_http = Config.URL_HTTP
        self.url_wss = Config.URL_WSS
    
    def connect(self):
        try:
            w3 = Web3(Web3.HTTPProvider(self.url_http))
        except:            
            try:
                w3 = Web3(Web3.WebsocketProvider(self.url_wss))
            except:
                raise SocketProviderError
            raise HttpProviderError
        
        return w3.isConnected()

class ETHClient:
    def __init__(self):
        pass