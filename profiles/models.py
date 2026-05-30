from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.full_name