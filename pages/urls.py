from django.urls import path
from .views import HomePageView, DashboardView,daily_activitiesView,ProgressAnalyticsView,MoodTrackerView,ProfileView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("dashboard/daily_activities/", daily_activitiesView.as_view(),name="daily_activities"),
    path("dashboard/progress/", ProgressAnalyticsView.as_view(), name="progress"),
    path("dashboard/mood-tracker/", MoodTrackerView.as_view(), name="mood_tracker"),
    path("dashboard/profile/", ProfileView.as_view(), name="profile"),
]
