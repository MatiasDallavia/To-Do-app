# Third-party Libraries
import strawberry
from asgiref.sync import sync_to_async
from strawberry.types.info import Info
from typing import List
from apps.tasks.models.tasks import Tasks , SubTasks

# Own Libraries
from apps.tasks.controllers.task_controller import SingleTasksController , ListTaskController
from apps.tasks.controllers.sub_task_controller import SingleSubTasksController , ListSubTasksController
from apps.tasks.schema.nodes.task_node import TaskNode , ListSubTaskNode , ListTaskNode


@strawberry.type
class TaskQuery:
    @strawberry.field(description="List of tasks")
    @sync_to_async
    def single_task(
        self,
        info: Info,
        task_id: strawberry.ID,
    ) -> TaskNode:
        reward_list_controller = SingleTasksController(task_id=int(task_id))
        task = reward_list_controller.get_object()
        return TaskNode.from_db_model(task)
    

@strawberry.type
class SingleSubTaskQuery:
    @strawberry.field(description="List of sub-tasks")
    @sync_to_async
    def single_subTask(
        self,
        info: Info,
        task_id: strawberry.ID,
    ) -> TaskNode:
        reward_list_controller = SingleSubTasksController(subTask_id=int(task_id))
        task = reward_list_controller.get_object()
        print(task)
        return TaskNode.from_db_model(task)
    

@strawberry.type
class ListTaskQuery:
    @strawberry.field(description="List of tasks")
    @sync_to_async
    def list_task() -> ListTaskNode:
        list_task_node = [ListSubTaskNode]
        tasks = ListTaskController.get_object_list()
        for task in tasks:
            reward_list_controller = ListSubTasksController(task=task)
            subTasks = reward_list_controller.get_object_list()
            sub_task_node = ListSubTaskNode.from_db_model(task, subTasks)
            list_task_node.append(sub_task_node)
        print(type(list_task_node))     
        print("subs: " ,list_task_node)       
        return ListTaskNode( task = list_task_node )    

                
    

@strawberry.type
class ListSubTaskQuery:
    @strawberry.field(description="List of sub-tasks")
    @sync_to_async
    def list_subTask(
        self,
        info: Info,
        task_id: strawberry.ID,
    ) -> ListSubTaskNode:
        reward_single_controller = SingleTasksController(task_id=int(task_id))
        task =  reward_single_controller.get_object()
        reward_list_controller = ListSubTasksController(task=task)
        subTasks = reward_list_controller.get_object_list()
        return ListSubTaskNode.from_db_model(task, subTasks)


@strawberry.type
class StateQuery:
    @strawberry.field(description="List of tasks")
    @sync_to_async
    def get_state(
        self,
        info: Info,
        task_id: strawberry.ID,
    ) -> bool:
        reward_list_controller = SingleTasksController(task_id=int(task_id))
        task = reward_list_controller.get_object()
        return TaskNode.from_db_model(task).is_completed

