# Standard Libraries
import logging
from typing import Optional, TypeVar , List
from apps.tasks.models.tasks import Tasks, SubTasks
from asgiref.sync import sync_to_async


import strawberry

from apps.core.schema.nodes.core_node import CoreNode

logger = logging.getLogger(__name__)


NodeType = TypeVar("NodeType")


@strawberry.type
class TaskNode:
    id: Optional[strawberry.ID] = None
    text: Optional[str] = None
    is_completed: Optional[bool] = None

    @classmethod
    def from_db_model(cls, instance):
        return cls(
            id=instance.id,
            text=instance.text,
            is_completed=instance.is_completed,
        )


@strawberry.type
class ListSubTaskNode(TaskNode):
    sub_tasks : List[TaskNode]

    @classmethod
    def from_db_model(cls, task: Tasks , sub_tasks_query):
        li = []
        for subTask in sub_tasks_query:
            li.append(subTask)
        print(li)           
        return cls(
            id=task.id,
            text=task.text,
            is_completed=task.is_completed,
            sub_tasks = li
        )

@strawberry.type
class ListTaskNode(TaskNode):
    tasks : List[ListSubTaskNode]

@strawberry.type
class TaskMutationNode(CoreNode):
    task: Optional[TaskNode] = strawberry.field(description="Created task")
