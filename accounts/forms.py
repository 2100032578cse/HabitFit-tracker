from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Only include fields needed at signup
        fields = (
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Include fields to be updated in the profile
        fields = (
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "weight",
            "height",
            "fitness_goals",
            "profile_picture",
        )
