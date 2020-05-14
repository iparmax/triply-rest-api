from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class TripManager(BaseUserManager):
    """Manager for user profiles"""

    def create_trip_info(self, email, user_id,origin,destination,dep_time):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        trip_info = self.model(email=email, user_id=user_id, origin=origin,destination = destination,dep_time = dep_time)

        trip_info.save(using=self._db)

        return trip_info


class Trip(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    user_id = models.CharField(max_length=255)
    origin = models.CharField(max_length=50,default="(38.00000,27.00000)")
    destination = models.CharField(max_length=50,default="(38.00000,27.00000)")
    dep_time = models.CharField(max_length=5,default="7:30")
    objects = TripManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id','origin','destination','dep_time']
