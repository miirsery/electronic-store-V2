from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    avatar = ProcessedImageField (upload_to='avatar',
                                      processors=[ResizeToFill(36, 36)],
                                      format='JPEG',
                                      options={'quality': 60},
                                      blank=True,
                                      null=True)
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    