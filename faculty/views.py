# faculty/views.py
from django.views.generic import CreateView, UpdateView
from .models import Marks

class MarksCreateView(CreateView):
    model = Marks
    fields = '__all__'  # Adjust fields as per your requirements
    template_name = 'faculty/marks_form.html'  # Replace with your template
    success_url = '/faculty/marks/'  # Replace with your success URL

class MarksUpdateView(UpdateView):
    model = Marks
    fields = '__all__'  # Adjust fields as per your requirements
    template_name = 'faculty/marks_form.html'  # Replace with your template
    success_url = '/faculty/marks/'  # Replace with your success URL





