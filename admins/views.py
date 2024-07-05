# admins/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Student, Faculty

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'  # Adjust fields as per your requirements
    template_name = 'admins/student_form.html'  # Replace with your template
    success_url = '/admin/students/'  # Replace with your success URL

class FacultyCreateView(CreateView):
    model = Faculty
    fields = '__all__'  # Adjust fields as per your requirements
    template_name = 'admins/faculty_form.html'  # Replace with your template
    success_url = '/admin/faculties/'  # Replace with your success URL



