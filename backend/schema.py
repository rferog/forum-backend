import graphene
import users.schema
import rferog.schema

class Query(users.schema.Query, rferog.schema.Query, graphene.ObjectType):
    pass

class Mutation(
    users.schema.Mutation,
    rferog.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
