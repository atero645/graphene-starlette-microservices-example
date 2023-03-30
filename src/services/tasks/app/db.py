from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base


Base = declarative_base()

binds = {
    Base: create_engine("sqlite+pysqlite:///db1.db?check_same_thread=False", echo=True, future=True),
}

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, binds=binds)
)

# session = sessionmaker()
# session.configure(binds=binds)

Base.query = db_session.query_property()

def init_db():
    from .models import Task

    Base.metadata.drop_all(bind=binds[Base], checkfirst=True)
    Base.metadata.create_all(bind=binds[Base], checkfirst=True)
    
    task1 = Task(name="Task1")
    task2 = Task(name="Task2")
    task3 = Task(name="Task3")
    
    db_session.add(task1)
    db_session.add(task2)
    db_session.add(task3)
    db_session.commit()
