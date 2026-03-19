from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    ROLE_CHOICE = (
        ('admin','Admin'),
        ('member','Member')
    )

    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='foto_perfil')
    role = models.CharField(max_length=20,choices=ROLE_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_full_name()