from django.contrib.auth import models as user_model
from django.db import models

from core import models as core_models


# Create your models here.

class Status(core_models.BaseModel):
    title = models.CharField(max_length=128, blank=True)
    color = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return f'{self.title}'


class Task(core_models.BaseModel):
    title = models.CharField(max_length=128, blank=True)
    text = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.status}'


class Comment(core_models.BaseModel):
    owner = models.ForeignKey(user_model.User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.owner.username} | {self.created}'
