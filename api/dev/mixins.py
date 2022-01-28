from web3 import Web3
from .providerTypes import GlobalProviderType

class Controller:
    def __init__(self, url):
        self.url: GlobalProviderType.addy = url
    
    def connection(self):
        return self


class WalletController:
    def __init__(self,):
        pass
    
    def account(self):
        pass
    
    def balance(self):
        pass
