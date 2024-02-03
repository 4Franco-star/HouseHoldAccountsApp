from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

CustomUser = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth")
        widgets = {
            'date_of_birth': forms.NumberInput(attrs={
                "type": "date"
            })
        }