from django.contrib import admin
from tasks import models
# Register your models here.


@admin.register(models.Task)
class TaskAdminModel(admin.ModelAdmin):
    pass