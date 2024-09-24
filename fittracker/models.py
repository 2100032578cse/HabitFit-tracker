from django.db import models
from django.conf import settings
from django.utils import timezone

CustomUser = settings.AUTH_USER_MODEL


class Goal(models.Model):
    STATUS_CHOICES = [
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("pending", "Pending"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_date = models.DateField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    target_duration = models.IntegerField(
        help_text="Total duration required to complete the goal in minutes"
    )
    challenge = models.ForeignKey(
        "Challenge",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="goals",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def mark_as_completed(self):
        self.status = "completed"
        self.save()
        Achievement.create_from_goal(self.user, self)  # Trigger an achievement

    def __str__(self):
        return f"{self.user.first_name} - {self.title}"


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ("exercise", "Exercise"),
        ("meditation", "Meditation"),
        ("reading", "Reading"),
        ("healthy_eating", "Healthy Eating"),
        ("hydration", "Hydration"),
        ("sleep", "Sleep"),
        ("medicine", "Medicine"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} - {self.activity_type} for {self.goal.title} on {self.date}"


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
    goal = models.OneToOneField(
        Goal, on_delete=models.CASCADE, related_name="challenge_goal"
    )

    def __str__(self):
        return self.title


class Achievement(models.Model):
    ACHIEVEMENT_TYPES = [
        ("streak", "Streak Achievement"),
        ("activity_minutes", "Activity Minutes Achievement"),
        ("challenges", "Challenge Achievement"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    achievement_type = models.CharField(max_length=50, choices=ACHIEVEMENT_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_achieved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user}"

    @staticmethod
    def create_from_goal(user, goal):
        # Example achievement for completing a goal
        achievement = Achievement(
            user=user,
            achievement_type="streak",
            title=f"Completed Goal: {goal.title}",
            description=f'You successfully completed the goal "{goal.title}".',
        )
        achievement.save()

    @staticmethod
    def create_from_activity_minutes(user, total_minutes):
        if total_minutes >= 1000:
            achievement = Achievement(
                user=user,
                achievement_type="activity_minutes",
                title="1000 Total Activity Minutes",
                description=f"Congratulations on reaching 1000 total activity minutes!",
            )
            achievement.save()

    @staticmethod
    def create_from_challenges(user, challenges_completed):
        if challenges_completed >= 5:
            achievement = Achievement(
                user=user,
                achievement_type="challenges",
                title="Completed 5 Challenges",
                description="You have successfully completed 5 challenges this month!",
            )
            achievement.save()


class WeeklyReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_data = models.JSONField()  # Store the report data as JSON
    report_date = models.DateField(
        default=timezone.now
    )  # Date when the report was generated

    class Meta:
        ordering = ["-report_date"]  # Order by newest reports

    def __str__(self):
        return f"Weekly Report for {self.user} - {self.report_date}"
