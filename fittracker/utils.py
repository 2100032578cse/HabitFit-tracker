from django.db.models import Avg
from .models import Goal, Activity


def get_goal_completion(user):
    user_goals = Goal.objects.filter(user=user)
    completed_goals = user_goals.filter(status="completed").count()
    remaining_goals = user_goals.exclude(status="completed").count()
    return completed_goals, remaining_goals


def get_activity_breakdown(user):
    activities = Activity.objects.filter(user=user)
    activity_data = {
        "exercise": activities.filter(activity_type="exercise").count(),
        "meditation": activities.filter(activity_type="meditation").count(),
        "reading": activities.filter(activity_type="reading").count(),
        "healthy_eating": activities.filter(activity_type="healthy_eating").count(),
    }
    return activity_data


def get_average_daily_activity(user):
    activities = Activity.objects.filter(user=user)
    return activities.aggregate(Avg("duration"))["duration__avg"] or 0


def get_progress_over_time(activities):
    return [
        activities.filter(date__month=1).aggregate(Avg("duration"))["duration__avg"]
        or 0,
        activities.filter(date__month=2).aggregate(Avg("duration"))["duration__avg"]
        or 0,
        activities.filter(date__month=3).aggregate(Avg("duration"))["duration__avg"]
        or 0,
        activities.filter(date__month=4).aggregate(Avg("duration"))["duration__avg"]
        or 0,
    ]


def calculate_longest_streak(activities):
    # Replace with your actual logic
    return 14


def calculate_most_active_day(activities):
    # Replace with your actual logic
    return "Monday"
