from django.views.generic import TemplateView
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Activity, Goal, Challenge, Mood, Achievement, WeeklyReport
from .forms import ActivityForm, GoalForm, ChallengeForm, MoodForm
from django.db.models import Sum
from .utils import (
    get_goal_completion,
    get_activity_breakdown,
    get_average_daily_activity,
    get_progress_over_time,
    calculate_longest_streak,
    calculate_most_active_day,
)


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

        # Calculate goal progress
        goal_progress = {}
        for goal in context["recent_goals"]:
            total_duration = (
                Activity.objects.filter(
                    user=self.request.user,
                    date__lte=goal.target_date,  # Optional: Limit by target date
                    goal=goal,  # Assuming you have a ForeignKey in Activity
                ).aggregate(total=Sum("duration"))["total"]
                or 0
            )

            goal_progress[goal.id] = (
                (total_duration / goal.target_duration) * 100
                if goal.target_duration
                else 0
            )

        context["goal_progress"] = goal_progress
        return context


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy("daily_activities")

    def form_valid(self, form):
        # Link the activity to the logged-in user
        form.instance.user = self.request.user
        # Link the activity to the specific goal, if provided
        goal_id = self.request.POST.get("goal")
        if goal_id:
            form.instance.goal = Goal.objects.get(id=goal_id, user=self.request.user)
        return super().form_valid(form)


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    success_url = reverse_lazy("daily_activities")

    def form_valid(self, form):
        # Link the goal to the logged-in user
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
        return Mood.objects.filter(user=self.request.user).order_by("-date")[:5]


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

        # Fetch user's activities
        activities = Activity.objects.filter(user=self.request.user)

        # Use utility functions to gather data
        completed_goals, remaining_goals = get_goal_completion(self.request.user)
        activity_data = get_activity_breakdown(self.request.user)
        average_daily_activity = get_average_daily_activity(self.request.user)
        progress_over_time = get_progress_over_time(activities)

        # Key metrics
        context["average_daily_activity"] = average_daily_activity
        context["longest_streak"] = calculate_longest_streak(activities)
        context["total_challenges_completed"] = Goal.objects.filter(
            user=self.request.user, challenge__isnull=False, status="completed"
        ).count()
        context["most_active_day"] = calculate_most_active_day(activities)

        # Add data to the context
        context["goal_completion"] = {
            "completed": completed_goals,
            "remaining": remaining_goals,
        }
        context["activity_breakdown"] = activity_data
        context["progress_over_time"] = progress_over_time

        # Fetch recent achievements
        context["recent_achievements"] = Achievement.objects.filter(
            user=self.request.user
        )[:5]

        return context


class LeaderboardView(LoginRequiredMixin, TemplateView):
    template_name = "fittracker/leaderboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add logic to fetch and process leaderboard data
        return context


class WeeklyReportView(LoginRequiredMixin, TemplateView):
    template_name = "report/weekly_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Get the latest report for the logged-in user
        latest_report = WeeklyReport.objects.filter(user=user).first()

        if latest_report:
            context["report"] = latest_report.report_data
            context["report_date"] = latest_report.report_date
        else:
            context["no_report"] = True
        return context
