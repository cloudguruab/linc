import graphene
from .dev.mixins import NodeMixin
from graphene import Schema
from .config import Config

TRIGGER = NodeMixin()

class Query(graphene.ObjectType):    
    get_balance = graphene.String(at=graphene.String(default_value=Config.DEMO_ACCT))
    lst_acct = graphene.String()
    
    def resolve_get_balance(root, info, at):
        balance = TRIGGER.get_balance(at)
        return f'Your current account balance is: {balance}'
    
    def resolve_lst_acct(root, info):
        accounts = TRIGGER.lst_accounts()
        return f'Current accounts: {accounts}'

class CreateWallet(graphene.Mutation):
    class Arguments:
        add = graphene.Boolean()
    
    data = graphene.String()    
        
    def mutate(root, info, add):
        account_transaction = TRIGGER.create_acct(add)
        return CreateWallet(data=account_transaction)
    
class Mutation(graphene.ObjectType):
    create_wallet = CreateWallet.Field()

schema = Schema(query=Query, mutation=Mutation)