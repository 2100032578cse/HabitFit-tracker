from django.urls import path
from .views import SignUpView, ProfileUpdateView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
