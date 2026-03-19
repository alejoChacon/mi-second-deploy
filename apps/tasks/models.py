from django.db import models

# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
        ('todo',"To Do"),
        ("in_progress","In Progress"),
        ("done","Done")
    ]

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    project = models.ForeignKey('projects.Project',on_delete=models.CASCADE,related_name='tasks')
    assigned_to = models.ForeignKey('users.User',on_delete=models.SET_NULL,null=True,blank=True,related_name='tareas')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='todo')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
