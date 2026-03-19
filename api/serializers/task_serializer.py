from rest_framework import serializers
from apps.tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    #project_name = serializers.CharField(source='project.name',read_only=True)
    #assigned_username = serializers.CharField(source='assigned_to.username',read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Id': instance.id,
            'Titulo': instance.title,
            'Descripcion': instance.description,
            'Estatus': instance.get_status_display(),
            'Fecha': instance.created_at,
            'Proyecto': instance.project.name,
            'Asignado A': instance.assigned_to.get_full_name() if instance.assigned_to else 'N/A'
        }