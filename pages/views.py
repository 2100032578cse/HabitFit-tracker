from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"