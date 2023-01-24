from django.contrib import admin

from tasks import models


# Register your models here.


class CommentInline(admin.TabularInline):
    model = models.Comment
    can_delete = False
    readonly_fields = ['owner', 'text', 'task']
    extra = 0


@admin.register(models.Task)
class TaskAdminModel(admin.ModelAdmin):
    inlines = [CommentInline]
    pass


@admin.register(models.Comment)
class CommentAdminModel(admin.ModelAdmin):
    pass


@admin.register(models.Status)
class StatusAdminModel(admin.ModelAdmin):
    pass
