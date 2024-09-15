from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home_page")
