from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"
class daily_activitiesView(TemplateView):
    template_name = "pages/daily_activities.html"

class MoodTrackerView(TemplateView):
    template_name = "pages/mood_tracker.html"

class ProfileView(TemplateView):
    template_name = "pages/profile.html"

class ProgressAnalyticsView(TemplateView):
    template_name = "pages/progress.html"
