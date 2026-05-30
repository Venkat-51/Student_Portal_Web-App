from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'dob', 'mobile', 'college', 'degree', 'profile_picture']