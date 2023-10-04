from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """Custom User class"""

    def __str__(self) -> str:
        return self.username