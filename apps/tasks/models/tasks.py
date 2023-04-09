from django.db import models


class Tasks(models.Model):
    text = models.TextField(blank=False, null=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task {self.id}"
    

class SubTasks(Tasks):
    task = models.ForeignKey(Tasks , related_name = "main_task" , on_delete = models.CASCADE) 

    def __str__(self):
        return f"Task {self.task.id}"


                
