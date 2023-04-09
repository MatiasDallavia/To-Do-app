import strawberry

from apps.tasks.schema.mutations.create_task import CreateTask
from apps.tasks.schema.queries.get_tasks import TaskQuery


@strawberry.type
class TasksQuery(TaskQuery):
    pass


@strawberry.type
class TasksMutation(CreateTask):
    pass
