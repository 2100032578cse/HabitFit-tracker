from django.contrib import admin
from .models import Activity, Goal, Mood, Challenge, Achievement


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "activity_type", "duration", "date")
    list_filter = ("activity_type", "date")
    search_fields = ("user__first_name", "user__last_name", "activity_type")


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "target_date", "completed", "completion_date")
    list_filter = ("completed", "target_date")
    search_fields = ("user__first_name", "user__last_name", "title")


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ("user", "mood", "date", "recommendation")
    list_filter = ("mood", "date")
    search_fields = ("user__first_name", "user__last_name")


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")
    search_fields = ("title",)
    filter_horizontal = ("participants",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ["title", "user"]
    search_fields = ["title"]
