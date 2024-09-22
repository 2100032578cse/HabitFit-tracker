from django import forms
from .models import Activity, Goal, Mood, Challenge


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["activity_type", "duration", "date"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["title", "description", "target_duration", "target_date"]
        widgets = {
            "target_date": forms.DateInput(attrs={"type": "date"}),
        }


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ["mood", "date", "recommendation"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ["title", "goal", "description", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
