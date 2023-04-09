import strawberry
from typing import List, Optional
from django.conf import settings

# settings.configure(DJANGO_SETTINGS_MODULE="task_exercise.settings")


# Reader, you can safely ignore Query in this example, it is required by
# strawberry.Schema so it is included here for completenes

import django
django.setup()

from apps.tasks.schema.mutations.create_task import CreateTask , CreateSubTask
from apps.tasks.schema.mutations.update_task import UpdateTask , UpdateSubTask
from apps.tasks.schema.queries.get_tasks import TaskQuery, StateQuery , SingleSubTaskQuery , ListSubTaskQuery , ListTaskQuery
from apps.tasks.schema.nodes.task_node import TaskNode




@strawberry.type
class Book:
    title: str 
    author: str

books = [
Book(title="book #1", author="jorge"),
Book(title="book #2", author="jorge"),
Book(title="book #3", author="pepe"),
Book(title="book #4", author="carlos")
]
    

@strawberry.type
class Query(StateQuery , TaskQuery , SingleSubTaskQuery , ListSubTaskQuery ,  ListTaskQuery):
    pass


    
@strawberry.type
class Mutation(CreateTask , UpdateTask , CreateSubTask , UpdateSubTask):
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f"Adding {title} by {author}")
        book = Book(title=title, author=author) 
        books.append(book)
        print(books)
        return book

schema = strawberry.Schema( 
                            mutation=Mutation ,
                            query =  Query,
                            ) 