from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate

class UserRgisterationForm(UserCreationForm):

    class Meta:
        model=User
        fields=('email','password1','passwoed2')


class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        email=cleaned_data.get("email")
        password=cleaned_data.get("password")

        if email and password:
            user=authenticate(
                username=email,
                password=password
            )

            if user is None:
                raise forms.ValidationError(
                    "One of fields is wrong"
                )

            cleaned_data["user"]=user

        return cleaned_data