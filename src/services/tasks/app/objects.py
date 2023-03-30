from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
from graphene_federation import key
from .models import Task

@key('id')
class TaskObject(SQLAlchemyObjectType):
    class Meta:
        model = Task
        interfaces = (graphene.relay.Node,)

