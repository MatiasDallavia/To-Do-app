# settings.configure(DJANGO_SETTINGS_MODULE="task_exercise.settings")


# Reader, you can safely ignore Query in this example, it is required by
# strawberry.Schema so it is included here for completenes

import django
import os
from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = "task_exercise.settings"
django.setup()

import strawberry
from django.conf import settings

from apps.tasks.schema.mutations.create_task import CreateTask , CreateSubTask
from apps.tasks.schema.mutations.update_task import UpdateTask , UpdateSubTask
from apps.tasks.schema.queries.get_tasks import TaskQuery , SingleSubTaskQuery , ListSubTaskQuery , ListTaskQuery


@strawberry.type
class Query( TaskQuery , SingleSubTaskQuery , ListSubTaskQuery ,  ListTaskQuery):
    pass


    
@strawberry.type
class Mutation(CreateTask , UpdateTask , CreateSubTask , UpdateSubTask):
    pass

schema = strawberry.Schema( 
                            mutation=Mutation ,
                            query =  Query,
                            ) 