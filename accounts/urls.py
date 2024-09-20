from django.urls import path
from .views import (
    SignUpView,
    ProfileUpdateView,
    CustomLoginView,
    CustomLogoutView,
    ProfilePageDetailView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("user/profile/", ProfilePageDetailView.as_view(), name="view_profile"),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
