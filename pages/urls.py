from django.urls import path
from .views import HomePageView, DashboardView, ProfileView,AboutView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("dashboard/about/", AboutView.as_view(), name="about"),
    path("about/", AboutView.as_view(), name="about"),
]
