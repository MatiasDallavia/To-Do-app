# Standard Libraries
import logging
from typing import Optional

import strawberry
from strawberry.types.info import Info

from apps.tasks.factories.concrete_factories.task_factory import (
    CreateTaskFactory, CreateSubTaskFactory
)
from apps.tasks.factories.concrete_factories.sub_task_factory import CreateSubTaskFactory

from apps.tasks.schema.nodes.task_node import TaskMutationNode , TaskNode

logger = logging.getLogger(__name__)


@strawberry.type
class CreateTask:   
    @strawberry.mutation
    async def create_task(
        self,
        info: Info,
        text: str,  
        is_completed: Optional[bool] = False,
    ) -> TaskMutationNode:
        try:
            factory = CreateTaskFactory(
                text=text,
                is_completed=is_completed,
            )
            task = await factory.create()
            success = True
            message = "Task created successfully"
            exception = None
        except Exception as e:
            success = False
            task = None
            message = f"An error occurred: {e}"
            exception = e
        return TaskMutationNode(
            success=success,
            message=message,
            error=exception,
            task=task,
        )


@strawberry.type
class CreateSubTask:
    @strawberry.mutation
    async def create_subTask(
        self,
        info: Info,
        task_id: strawberry.ID, 
        text: str,  
        is_completed: Optional[bool] = False,
    ) -> TaskMutationNode:
        try:
            subTask = None
            print("*"* 30)
            factory = CreateSubTaskFactory(
                task_id= task_id,
                text=text,
                is_completed=is_completed,
            )
            print("-"* 30)
            subTask = await factory.create()
            success = True
            message = "Task created successfully"
            exception = None
        except Exception as e:
            success = False
            task = None
            message = f"An error occurred: {e}"
            exception = e
            print(subTask)
            print(type(subTask))
        return TaskMutationNode(
            success=success,
            message=message,
            error=exception,
            task=subTask,
        )    



        
