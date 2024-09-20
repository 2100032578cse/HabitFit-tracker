from django.views.generic import TemplateView
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Activity, Goal, Challenge, Mood
from .forms import ActivityForm, GoalForm, ChallengeForm, MoodForm


class DailyActivitiesView(LoginRequiredMixin, TemplateView):
    template_name = "fittracker/daily_activities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activity_form"] = ActivityForm()
        context["goal_form"] = GoalForm()
        context["recent_activities"] = Activity.objects.filter(
            user=self.request.user
        ).order_by("-date")[:5]
        context["recent_goals"] = Goal.objects.filter(
            user=self.request.user, completed=False
        ).order_by("target_date")[:5]
        return context


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy("daily_activities")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    success_url = reverse_lazy("daily_activities")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MoodListView(LoginRequiredMixin, ListView):
    model = Mood
    template_name = "fittracker/mood_list.html"
    context_object_name = "moods"

    def get_queryset(self):
        return Mood.objects.filter(user=self.request.user).order_by("-date")


class MoodCreateView(LoginRequiredMixin, CreateView):
    model = Mood
    form_class = MoodForm
    template_name = "fittracker/mood_form.html"
    success_url = reverse_lazy("mood-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChallengeListView(LoginRequiredMixin, ListView):
    model = Challenge
    template_name = "fittracker/challenge_list.html"
    context_object_name = "challenges"


class ChallengeCreateView(LoginRequiredMixin, CreateView):
    model = Challenge
    form_class = ChallengeForm
    template_name = "fittracker/challenge_form.html"
    success_url = reverse_lazy("challenge-list")


class ProgressView(LoginRequiredMixin, TemplateView):
    template_name = "fittracker/progress.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add logic to fetch and process progress data
        return context


class LeaderboardView(LoginRequiredMixin, TemplateView):
    template_name = "fittracker/leaderboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add logic to fetch and process leaderboard data
        return context
