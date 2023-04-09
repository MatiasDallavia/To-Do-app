from apps.core.interfaces.base_interfaces import CreateInstance, SingleQuery, ListQuery
from apps.tasks.models.tasks import Tasks , SubTasks

from asgiref.sync import sync_to_async


class ListSubTasksController(ListQuery):
    def __init__(self, task: Tasks):
        self.task_id = task.id
        self.model = SubTasks

    def get_object_list(self):
        return self.model.objects.filter(task_id = self.task_id)
    


class SingleSubTasksController(SingleQuery):
    def __init__(self, subTask_id: int):
        self.task_id = subTask_id
        self._model = SubTasks

    def get_object(self):
        return self._model.objects.filter(id=self.task_id).first()
    

class CreateSubTaskController(CreateInstance):

    def __init__(self, task_id: int , text: str, is_completed: bool = False):
        self.task_id = task_id
        self.text = text
        self.is_completed = is_completed
        self._model = SubTasks

    def create(self):
        return self._model.objects.create(
            task = Tasks.objects.filter(id = self.task_id).first(), 
            text=self.text,
            is_completed=self.is_completed
        )