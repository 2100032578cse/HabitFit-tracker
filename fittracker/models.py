from django.db import models
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ("exercise", "Exercise"),
        ("meditation", "Meditation"),
        ("reading", "Reading"),
        ("healthy_eating", "Healthy Eating"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} - {self.activity_type} on {self.date}"


class Goal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_date = models.DateField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.title}"


class Mood(models.Model):
    MOOD_CHOICES = [
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Neutral"),
        (4, "Good"),
        (5, "Very Good"),
        (6, "Excited"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mood = models.IntegerField(choices=MOOD_CHOICES)
    date = models.DateField()
    recommendation = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.first_name} - Mood on {self.date}"


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(CustomUser, related_name="challenges")

    def __str__(self):
        return self.title
