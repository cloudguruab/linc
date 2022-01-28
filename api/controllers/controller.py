from web3 import Web3
from ..dev.mixins import Controller
from ..dev.providerTypes import GlobalProviderType

class HttpProvider(Controller):
    """
    HTTP connection to blockchain. Support for web based connections, 
    and integrations for remote node providers. 
    """
    def __init__(self, provider):
        self.provider: GlobalProviderType.addy = provider
        
    def __str__(self):
        return f'<Http Provider> {self.provider}'
    
    def __repr__(self):
        return f'<Http Provider> {self.provider}'
    
    
class IpcProvider(Controller):
    """
    IPC connection to blockchain. For running local nodes IPC provider
    is the most secure connection type.
    """
    def __init__(self, provider):
        self.provider: GlobalProviderType.addy = provider
        
    def __str__(self):
        return f'<IPC Provider> {self.provider}'
    
    def __repr__(self):
        return f'<IPC Provider> {self.provider}'
  
    
class SocketProvider(Controller):
    """
    Web Socket connection to blockchain. Support for web based connections
    and supports remote node providers as well.
    """
    def __init__(self, provider):
        self.provider: GlobalProviderType.addy = provider\
            
    def __str__(self):
        return f'<Web Socket Provider> {self.provider}'
    
    def __repr__(self):
        return f'<Web Socket Provider> {self.provider}'