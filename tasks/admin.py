from idlelib.searchengine import search_reverse

from django.contrib import admin

# Register your models here.
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name','description')



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'executor', 'status', 'created_at')
    list_filter = ('status', 'project')
    list_editable = ('status',)
    search_fields = ('title', 'description')
