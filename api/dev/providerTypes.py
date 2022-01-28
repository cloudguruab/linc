from enum import Enum

class GlobalProviderType(Enum):
    """
    configuration type for provider connections to web3 wallet.
    
    addy: string value for connections from settings 
        and permission suites inside wallet platform.
    
    """
    addy: str
    
class BlockchainActivityType(Enum):
    """
    configuration type for activities on chain through wyre api.
    """
    # get balance
    # looking up receipts
    # looking up transactions
    
    
