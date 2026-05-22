from rest_framework import serializers
from .models import Project, Task
class ProjectSerializer(serializers.ModelSerializer):
    manager_name = serializers.CharField(source='manager.username', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'manager', 'manager_name', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    executor_name = serializers.CharField(source= 'executor.username', read_only=True)
    class Meta:
        model = Task
        fields = [
            'id', 'project', 'title', 'description',
            'status', 'status_display', 'executor',
            'executor_name', 'created_at', 'updated_at'
        ]