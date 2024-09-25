from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
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
    bio = forms.CharField(required=False, widget=forms.Textarea)
    location = forms.CharField(required=False, max_length=100)

    class Meta:
        model = CustomUser
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

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        # Add UserProfile data to form initial values
        user_profile = self.instance.profile
        self.fields["bio"].initial = user_profile.bio
        self.fields["location"].initial = user_profile.location

    def save(self, commit=True):
        # Save CustomUser model first
        user = super(CustomUserChangeForm, self).save(commit=False)
        if commit:
            user.save()

        # Then save UserProfile data
        user_profile = user.profile
        user_profile.bio = self.cleaned_data["bio"]
        user_profile.location = self.cleaned_data["location"]
        user_profile.save()

        return user
