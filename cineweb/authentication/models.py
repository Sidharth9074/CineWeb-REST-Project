from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class RoleChoices(models.TextChoices):

    USER = 'User','User'

    ADMIN = 'Admin','Admin'

class Profile(AbstractUser):

    role = models.CharField(max_length=10,choices=RoleChoices.choices)

    class Meta :

        verbose_name = 'Profile' 

        verbose_name_plural = 'Profile'   


    def __str__(self):

        return f'{self.username}'        
