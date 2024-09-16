from django import forms
from .models import Activity, Goal, Mood, Challenge


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["activity_type", "duration", "date", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["title", "description", "target_date"]
        widgets = {
            "target_date": forms.DateInput(attrs={"type": "date"}),
        }


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ["mood", "date", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ["title", "description", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }