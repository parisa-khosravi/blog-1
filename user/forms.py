from .models import *
from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name','last_name',
                  'avatar','address','github_link']