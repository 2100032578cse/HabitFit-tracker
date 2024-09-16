from django.urls import path
from .views import (
    DailyActivitiesView,
    ProgressAnalyticsView,
    MoodTrackerView,
    CommunityChallengeView,
    ChallengeLeaderBoardView,
)

urlpatterns = [
    path(
        "dashboard/daily_activities/",
        DailyActivitiesView.as_view(),
        name="daily_activities",
    ),
    path("dashboard/progress/", ProgressAnalyticsView.as_view(), name="progress"),
    path("dashboard/mood-tracker/", MoodTrackerView.as_view(), name="mood_tracker"),
    path(
        "dashboard/challenge/",
        CommunityChallengeView.as_view(),
        name="community-challenge",
    ),
    path(
        "dashboard/leaderboard/",
        ChallengeLeaderBoardView.as_view(),
        name="challenge-leaderboard",
    ),
]


# urlpatterns = [
#     path('', DashboardView.as_view(), name='dashboard'),
#     path('daily-activities/', DailyActivitiesView.as_view(), name='daily_activities'),
#     path('activity/add/', ActivityCreateView.as_view(), name='activity_add'),
#     path('activity/<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity_edit'),
#     path('activity/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity_delete'),
#     path('progress/', ProgressAnalyticsView.as_view(), name='progress'),
#     path('mood-tracker/', MoodTrackerView.as_view(), name='mood_tracker'),
#     path('mood/add/', MoodCreateView.as_view(), name='mood_add'),
#     path('challenges/', CommunityChallengeView.as_view(), name='community-challenge'),
#     path('challenge/<int:pk>/join/', ChallengeJoinView.as_view(), name='challenge_join'),
#     path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
#     path('profile/', ProfileView.as_view(), name='profile'),
# ]
