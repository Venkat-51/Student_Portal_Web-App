from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'dob', 'mobile', 'college', 'degree', 'profile_picture']