import graphene
import pos_backend_app.schema

class Query(pos_backend_app.schema.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass
schema = graphene.Schema(query=Query)
