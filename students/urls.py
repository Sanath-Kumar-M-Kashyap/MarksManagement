# students/urls.py
from django.urls import path
from .views import StudentDetailView

urlpatterns = [
    path('profile/', StudentDetailView.as_view(), name='student-profile'),
    # Add more URLs as needed
]

