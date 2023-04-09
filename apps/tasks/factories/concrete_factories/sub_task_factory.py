from asgiref.sync import sync_to_async

import strawberry

from apps.tasks.controllers.sub_task_controller import CreateSubTaskController , ListSubTasksController
from apps.tasks.factories.abstract_interfaces import IConcreteFactory


class CreateSubTaskFactory(IConcreteFactory):
    def __init__(self, task_id: int , text: str, is_completed: bool):
        self.controller = CreateSubTaskController(
            task_id=task_id,
            text=text,
            is_completed=is_completed,
        )

    @sync_to_async
    def create(self):
        return self.controller.create()
    
    @sync_to_async
    def update(self):
        pass

class UpdateSubTaskFactory(IConcreteFactory):
    
    def __init__(self, subTask_id: int):
        self.controller = ListSubTasksController(subTask_id= subTask_id)

    @sync_to_async
    def create(self):
        pass        

    @sync_to_async
    def update(self, is_completed: bool):
        self.controller = self.controller.get_object()
        self.controller.is_completed = is_completed
        self.controller.save()
        return self.controller 

