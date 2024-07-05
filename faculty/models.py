# faculty/models.py
from django.db import models
from users.models import User
from admins.models import Student

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ia1 = models.DecimalField(max_digits=5, decimal_places=2)
    ia2 = models.DecimalField(max_digits=5, decimal_places=2)
    ia3 = models.DecimalField(max_digits=5, decimal_places=2)
    assignment1 = models.DecimalField(max_digits=5, decimal_places=2)
    assignment2 = models.DecimalField(max_digits=5, decimal_places=2)
    sub_code = models.CharField(max_length=20)
    cie_component = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.sub_code}"

class FacultySubject(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} - {self.sub_code}"


