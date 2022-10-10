from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("tickets:ticket-list")

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)

        return valid


class LogInView(SuccessMessageMixin, LoginView):
    next_page = reverse_lazy("tickets:ticket-list")
    template_name = "users/login.html"


class LogOutView(LogoutView):

    next_page = reverse_lazy("home:home")
