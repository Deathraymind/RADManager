from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)
    # Add more fields as needed
