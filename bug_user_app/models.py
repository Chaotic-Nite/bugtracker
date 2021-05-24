from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True, null=True)