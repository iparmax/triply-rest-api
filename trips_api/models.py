from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class TripManager(BaseUserManager):
    """Manager for tripd"""

    def create_trip_info(self,user_id,origin,destination,dep_time):
        """Create a new trip"""

        trip_info = self.model(user_id=user_id, origin=origin,destination = destination,dep_time = dep_time)

        trip_info.save(using=self._db)

        return trip_info


class Trip(AbstractBaseUser):
    """Database model for users in the system"""
    user_id = models.CharField(max_length=255)
    origin = models.CharField(max_length=50,default="(38.00000,27.00000)")
    destination = models.CharField(max_length=50,default="(38.00000,27.00000)")
    dep_time = models.CharField(max_length=5,default="7:30")
    objects = TripManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['origin','destination','dep_time']


class SuperUserManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, username, name, password=None):
        """Create a new user profile"""

        user = self.model(username=username, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(username, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class SuperUser(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    username = models.TextField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = SuperUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']