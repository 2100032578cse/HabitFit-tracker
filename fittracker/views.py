from django.views.generic import TemplateView


class DailyActivitiesView(TemplateView):
    template_name = "fittracker/daily_activities.html"


class MoodTrackerView(TemplateView):
    template_name = "fittracker/mood_tracker.html"


class ProgressAnalyticsView(TemplateView):
    template_name = "fittracker/progress.html"


class CommunityChallengeView(TemplateView):
    template_name = "fittracker/community_challenge.html"


class ChallengeLeaderBoardView(TemplateView):
    template_name = "fittracker/leaderboard.html"


# from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.db.models import Sum
# from django.utils import timezone
# from .models import Activity, Goal, Mood, Challenge, UserProfile
# from .forms import ActivityForm, GoalForm, MoodForm, ChallengeForm

# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = "fittracker/dashboard.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         today = timezone.now().date()

#         context['total_activities'] = Activity.objects.filter(user=user).count()
#         context['completed_goals'] = Goal.objects.filter(user=user, completed=True).count()
#         context['current_streak'] = user.profile.current_streak
#         context['total_points'] = user.profile.total_points
#         context['today_activities'] = Activity.objects.filter(user=user, date=today)
#         context['mood_today'] = Mood.objects.filter(user=user, date=today).first()

#         return context

# class DailyActivitiesView(LoginRequiredMixin, ListView):
#     model = Activity
#     template_name = "fittracker/daily_activities.html"
#     context_object_name = 'activities'

#     def get_queryset(self):
#         return Activity.objects.filter(user=self.request.user, date=timezone.now().date())

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = ActivityForm()
#         return context

# class ActivityCreateView(LoginRequiredMixin, CreateView):
#     model = Activity
#     form_class = ActivityForm
#     template_name = "fittracker/activity_form.html"
#     success_url = reverse_lazy('daily_activities')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class ActivityUpdateView(LoginRequiredMixin, UpdateView):
#     model = Activity
#     form_class = ActivityForm
#     template_name = "fittracker/activity_form.html"
#     success_url = reverse_lazy('daily_activities')

# class ActivityDeleteView(LoginRequiredMixin, DeleteView):
#     model = Activity
#     success_url = reverse_lazy('daily_activities')

# class ProgressAnalyticsView(LoginRequiredMixin, TemplateView):
#     template_name = "fittracker/progress.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user

#         # Get activities for the last 30 days
#         thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
#         activities = Activity.objects.filter(user=user, date__gte=thirty_days_ago)

#         context['total_duration'] = activities.aggregate(Sum('duration'))['duration__sum'] or 0
#         context['activity_count'] = activities.count()
#         context['goals_completed'] = Goal.objects.filter(user=user, completed=True, completion_date__gte=thirty_days_ago).count()
#         context['longest_streak'] = user.profile.longest_streak

#         # Activity breakdown
#         activity_types = activities.values('activity_type').annotate(total_duration=Sum('duration'))
#         context['activity_breakdown'] = list(activity_types)

#         # Progress over time (last 7 days)
#         seven_days_ago = timezone.now() - timezone.timedelta(days=7)
#         daily_progress = activities.filter(date__gte=seven_days_ago).values('date').annotate(total_duration=Sum('duration'))
#         context['daily_progress'] = list(daily_progress)

#         return context

# class MoodTrackerView(LoginRequiredMixin, ListView):
#     model = Mood
#     template_name = "fittracker/mood_tracker.html"
#     context_object_name = 'moods'

#     def get_queryset(self):
#         return Mood.objects.filter(user=self.request.user).order_by('-date')[:30]

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = MoodForm()
#         return context

# class MoodCreateView(LoginRequiredMixin, CreateView):
#     model = Mood
#     form_class = MoodForm
#     template_name = "fittracker/mood_form.html"
#     success_url = reverse_lazy('mood_tracker')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class CommunityChallengeView(LoginRequiredMixin, ListView):
#     model = Challenge
#     template_name = "fittracker/community_challenge.html"
#     context_object_name = 'challenges'

#     def get_queryset(self):
#         return Challenge.objects.filter(end_date__gte=timezone.now()).order_by('start_date')

# class ChallengeJoinView(LoginRequiredMixin, UpdateView):
#     model = Challenge
#     fields = []
#     template_name = "fittracker/challenge_join.html"
#     success_url = reverse_lazy('community-challenge')

#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.participants.add(self.request.user)
#         return super().form_valid(form)

# class LeaderboardView(LoginRequiredMixin, ListView):
#     model = UserProfile
#     template_name = "fittracker/leaderboard.html"
#     context_object_name = 'leaderboard'

#     def get_queryset(self):
#         return UserProfile.objects.all().order_by('-total_points')[:50]

# class ProfileView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     fields = ['bio', 'birthdate', 'location']
#     template_name = "fittracker/profile.html"
#     success_url = reverse_lazy('profile')

#     def get_object(self, queryset=None):
#         return self.request.user.profile
