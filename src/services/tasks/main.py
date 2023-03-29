import graphene
#from graphene_file_upload.scalars import Upload

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from graphene_federation import build_schema, key

@key('id')
class Task(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    tasks = graphene.List(Task)

    def resolve_tasks(root, info):
        return [
                {"id": "task1", "name": "Task1"},
                {"id": "task2", "name": "Task2"},
                {"id": "task3", "name": "Task3"},
            ]


app = Starlette()
schema = build_schema(query=Query)
#schema = graphene.Schema(query=Query, mutation=None, subscription=None)

app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE

# app.mount("/", GraphQLApp(schema, on_get=make_playground_handler()))  # Playground IDE
# app.mount("/", GraphQLApp(schema)) # no IDE