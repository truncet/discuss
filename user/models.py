from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy

# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, user_email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(user_email, user_name, password, **other_fields)

    def create_user(self, user_email, user_name, password, **other_fields):

        if not user_email:
            raise ValueError(gettext_lazy('You must provide an email address'))

        user_email = self.normalize_email(user_email)
        user = self.model(user_email=user_email,
                          user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=20, unique=True)
    user_email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(gettext_lazy('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name
