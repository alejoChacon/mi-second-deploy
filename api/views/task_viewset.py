from rest_framework.viewsets import ModelViewSet
from api.serializers.task_serializer import TaskSerializer
from apps.tasks.models import Task
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(ModelViewSet):
    
    serializer_class = TaskSerializer
    queryset = Task.objects.select_related('project','assigned_to').all()
    permission_classes = [IsAuthenticated]
    
    filterset_fields = ["status","project"]
