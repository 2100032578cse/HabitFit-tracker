from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from fittracker.models import Activity, Goal, Mood


class HomePageView(TemplateView):
    template_name = "pages/home.html"


# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = "pages/dashboard.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_activities"] = Activity.objects.filter(
            user=self.request.user
        ).order_by("-date")[:5]
        context["goals"] = Goal.objects.filter(user=self.request.user, completed=False)[
            :5
        ]
        context["recent_moods"] = Mood.objects.filter(user=self.request.user).order_by(
            "-date"
        )[:5]
        return context


class ProfileView(TemplateView):
    template_name = "pages/profile.html"
