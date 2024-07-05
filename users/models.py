# users/models.py
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class User(AbstractUser,PermissionsMixin):
    ROLES = (
        ('admin', 'Admin'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.username




