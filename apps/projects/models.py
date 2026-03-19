from django.db import models

# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    owner = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='owned_projects')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name