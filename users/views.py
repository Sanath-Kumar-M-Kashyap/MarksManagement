# users/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # Replace with your template

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


