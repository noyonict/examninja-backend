import graphene
from user_management.schema import Mutation as AuthMutation


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
