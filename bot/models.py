from django.db import models

class User(models.Model):
  user_key = models.CharField(max_length=50, unique=True)
  screen_name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

