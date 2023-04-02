import graphene
#from graphene_file_upload.scalars import Upload

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from graphene_federation import build_schema, key

@key('id')
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(root, info):
        return [
                {"id": "john", "name": "John"},
                {"id": "adam", "name": "Adam"},
                {"id": "alex", "name": "Alex"},
            ]


app = Starlette()
schema = build_schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=None, subscription=None)

app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE

# app.mount("/", GraphQLApp(schema, on_get=make_playground_handler()))  # Playground IDE
# app.mount("/", GraphQLApp(schema)) # no IDE