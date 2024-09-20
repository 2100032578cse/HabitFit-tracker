from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class ProfilePageDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = "pages/profile.html"
    context_object_name = "user_profile"

    def get_object(self):
        # Ensure the user has a profile, create if not
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile


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
