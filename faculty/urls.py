# faculty/urls.py
from django.urls import path
from .views import MarksCreateView, MarksUpdateView

urlpatterns = [
    path('marks/create/', MarksCreateView.as_view(), name='marks-create'),
    path('marks/<int:pk>/update/', MarksUpdateView.as_view(), name='marks-update'),
    # Add more URLs as needed
]

