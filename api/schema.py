import graphene
from .dev.mixins import NodeMixin
from graphene import Schema
from .config import Config

class Query(graphene.ObjectType):
    get_balance = graphene.String(at=graphene.String(default_value=Config.DEMO_ACCT))
    
    def resolve_get_balance(root, info, at):
        trigger = NodeMixin()
        balance = trigger.get_balance(at)
        return f'Your current account balance is: {balance}'

# class Mutation(graphene.Mutation):
#     pass

schema = Schema(query=Query)