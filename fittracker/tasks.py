from celery import shared_task
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Count, Sum, Avg
from datetime import timedelta
from .models import Activity, Goal, Mood, Achievement, WeeklyReport
from django.core.mail import send_mail

CustomUser = get_user_model()

import logging

logger = logging.getLogger(__name__)


@shared_task
def generate_weekly_report_for_all_users():
    today = timezone.now().date()
    week_start = today - timedelta(days=7)

    users = CustomUser.objects.all()
    for user in users:
        # Generate the report
        report = generate_weekly_report(user, week_start, today)
        # Save the report in the WeeklyReport model
        WeeklyReport.objects.create(user=user, report_data=report, report_date=today)

        # send email or store the report in the database
        # send_weekly_report_email(user, report)


def generate_weekly_report(user, week_start, today):
    # Query activities in the last 7 days
    activities = Activity.objects.filter(user=user, date__range=[week_start, today])
    activity_summary = activities.values("activity_type").annotate(
        total_duration=Sum("duration"), activity_count=Count("id")
    )

    # Query goals completed in the last 7 days
    goals = Goal.objects.filter(user=user, target_date__range=[week_start, today])
    goals_summary = goals.values("status").annotate(goal_count=Count("id"))
    completed_goals = goals.filter(status="completed").count()

    # Query moods for the last 7 days
    moods = Mood.objects.filter(user=user, date__range=[week_start, today])
    mood_avg = moods.aggregate(average_mood=Avg("mood"))["average_mood"] or "No data"
    mood_trend = (
        moods.values("mood").annotate(mood_count=Count("id")).order_by("-mood_count")
    )

    # Query achievements in the last 7 days
    achievements = Achievement.objects.filter(
        user=user, date_achieved__range=[week_start, today]
    )

    # Create the report
    report = {
        "activity_summary": list(activity_summary),
        "goals_summary": list(goals_summary),
        "completed_goals": completed_goals,
        "average_mood": mood_avg,
        "mood_trend": list(mood_trend),
        "achievements": [
            {
                "title": achievement.title,
                "date_achieved": achievement.date_achieved.strftime("%Y-%m-%d"),
            }
            for achievement in achievements
        ],
        "report_generated_on": today.strftime("%Y-%m-%d"),
    }

    return report


def send_weekly_report_email(user, report):
    subject = f"Your Weekly Report for {timezone.now().date()}"
    message = f"""
    Hi {user.first_name},

    Here's your progress report for the past week:

    Activities:
    {report['activity_summary']}

    Goals:
    Completed Goals: {report['completed_goals']}
    In Progress Goals: {report['goals_summary']}

    Mood:
    Average Mood: {report['average_mood']}
    Mood Trend: {report['mood_trend']}

    Achievements:
    {report['achievements']}

    Keep up the good work!
    """

    send_mail(subject, message, "noreply@habitfit.com", [user.email])
