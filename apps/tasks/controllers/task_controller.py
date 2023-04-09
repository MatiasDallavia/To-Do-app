from apps.core.interfaces.base_interfaces import CreateInstance, SingleQuery, ListQuery
from apps.tasks.models.tasks import Tasks


class CreateTaskController(CreateInstance):
    def __init__(self, text: str, is_completed: bool = False):
        self.text = text
        self.is_completed = is_completed
        self._model = Tasks

    def create(self):
        return self._model.objects.create(
            text=self.text,
            is_completed=self.is_completed,
        )


class SingleTasksController(SingleQuery):
    def __init__(self, task_id: int):
        self.task_id = task_id
        self._model = Tasks

    # @sync_to_async
    def get_object(self):
        return self._model.objects.filter(id=self.task_id).first()


class ListTaskController(ListQuery):
    model = Tasks 

    @classmethod
    def get_object_list(self):
        return self.model.objects.all()            

    



