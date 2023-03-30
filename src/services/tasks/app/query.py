from .objects import TaskObject
from graphene_sqlalchemy import SQLAlchemyConnectionField


TasksQueryField = SQLAlchemyConnectionField(TaskObject.connection)