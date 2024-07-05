# students/models.py
from django.db import models
from admins.models import Student as AdminStudent

class Student(models.Model):
    user = models.OneToOneField(AdminStudent, on_delete=models.CASCADE)
    # Add other fields as needed for student-specific details

    def __str__(self):
        return self.user.user.username





