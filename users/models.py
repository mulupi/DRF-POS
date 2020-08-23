# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

class UserManager(BaseUserManager):
 
    def _create_user(self, user_name, password, **extra_fields):
        """
        Creates and saves a User with the given user_name,and password.
        """
        if not user_name:
            raise ValueError('The given user_name must be set')
        try:
            with transaction.atomic():
                user = self.model(user_name=user_name, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_manager', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_name, password, **extra_fields)
    
    def create_manager(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_manager', True)
        return self._create_user(user_name, password, **extra_fields)
    def create_attandant(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_attendant', True)
        return self._create_user(user_name, password, **extra_fields)
 
    def create_superuser(self, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        return self._create_user(user_name, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    id_number=models.BigIntegerField(primary_key=True, unique=True)
    email = models.EmailField(max_length=40, unique=True, blank=False)
    user_name=models.CharField(max_length=30, unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_attendant = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    file_upload = models.ImageField(upload_to='images/') 
 
    objects = UserManager()
 
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'id_number']


    def isattandant(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_attendant
    def ismanager(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_manager
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self