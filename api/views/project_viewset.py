from rest_framework.viewsets import ModelViewSet
from apps.projects.models import Project
from api.serializers.project_serializer import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from ..permissions.is_owner import IsOwner

class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)