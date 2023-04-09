import logging
import strawberry
from apps.tasks.schema.nodes.task_node import TaskMutationNode , TaskNode
from apps.tasks.factories.concrete_factories.task_factory  import UpdateTaskFactory
from apps.tasks.factories.concrete_factories.sub_task_factory  import UpdateSubTaskFactory

logger = logging.getLogger(__name__)

@strawberry.type
class UpdateTask:
    @strawberry.mutation
    async def update_task( 
        self ,
        task_id: strawberry.ID ,
        is_completed : bool 
    ) -> TaskMutationNode:
        try:
            reward_list_controller = UpdateTaskFactory(task_id=int(task_id))
            task = await reward_list_controller.update(is_completed = is_completed)
            print("task: " , type(task))
            task = TaskNode.from_db_model(task)
            success = True
            message = "Task updated successfully"
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
class UpdateSubTask:
    @strawberry.mutation
    async def update_subTask( 
        self ,
        subTask_id: strawberry.ID ,
        is_completed : bool 
    ) -> TaskMutationNode:
        try:
            reward_list_controller = UpdateSubTaskFactory(subTask_id=int(subTask_id))
            subTask = await reward_list_controller.update(is_completed = is_completed)
            print("task: " , type(subTask))
            subTask = TaskNode.from_db_model(subTask)
            success = True
            message = "sub-Task updated successfully"
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
            task=subTask,
        )   