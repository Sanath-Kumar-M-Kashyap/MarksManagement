# students/views.py
from django.views.generic import DetailView
from admins.models import Student as AdminStudent

class StudentDetailView(DetailView):
    model = AdminStudent
    template_name = 'students/student_detail.html'  # Replace with your template
    context_object_name = 'student'

    def get_object(self, queryset=None):
        # Return the logged-in student's details
        return self.request.user.student



