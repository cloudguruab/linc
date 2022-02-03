import web3
from web3 import eth
from web3.auto.infura import w3
from ..controllers.providers import LocalProvider, HostedProvider


class NodeMixin:
    def __init__(self):
        self.w3 = w3
        
        if not self.w3.isConnected():
            self.w3 = HostedProvider().connect_http()
            
    def lst_accounts(self):
        return self.w3.eth.accounts

    def create_acct(self, *args):
        accounts_pool = self.lst_accounts()
        
        if not accounts_pool or args.add == True:
            acct = self.w3.eth.account.create()
            self.w3.eth.accounts.append(acct.address)
            return {'address': acct.address, 'key': acct.privateKey.hex()}

        return {'indicator': 'Please specify ADD to create an account',
                'account list': accounts_pool}
    
    def get_balance(self, address):
        return self.w3.eth.get_balance(address)