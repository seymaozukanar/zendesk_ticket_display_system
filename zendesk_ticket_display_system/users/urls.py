from django.urls import path
from .views import SignUpView, LogInView, LogOutView


urlpatterns = [
    path("sign-up", SignUpView.as_view(), name="signup"),
    path("log-in",  LogInView.as_view(), name="login"),
    path("log-out", LogOutView.as_view(), name="logout"),
]
