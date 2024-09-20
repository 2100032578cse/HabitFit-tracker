from django.urls import path
from .views import (
    DailyActivitiesView,
    MoodListView,
    MoodCreateView,
    ChallengeListView,
    ChallengeCreateView,
    ActivityCreateView,
    GoalCreateView,
    ProgressView,
    LeaderboardView,
)

urlpatterns = [
    path("daily-activities/", DailyActivitiesView.as_view(), name="daily_activities"),
    path("activity/create/", ActivityCreateView.as_view(), name="activity_create"),
    path("goal/create/", GoalCreateView.as_view(), name="goal_create"),
    path("moods/create/", MoodCreateView.as_view(), name="mood-create"),
    path("goals/create/", GoalCreateView.as_view(), name="goal-create"),
    path("moods/", MoodListView.as_view(), name="mood-list"),
    path("challenges/", ChallengeListView.as_view(), name="challenge-list"),
    path("challenges/create/", ChallengeCreateView.as_view(), name="challenge-create"),
    path("progress/", ProgressView.as_view(), name="progress"),
    path("leaderboard/", LeaderboardView.as_view(), name="leaderboard"),
]
