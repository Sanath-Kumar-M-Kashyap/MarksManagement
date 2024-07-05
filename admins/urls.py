# admins/urls.py
from django.urls import path
from .views import StudentCreateView, FacultyCreateView

urlpatterns = [
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('faculties/add/', FacultyCreateView.as_view(), name='faculty-add'),
    # Add more URLs as needed
]

