from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as UserManagerBase


class UserManager(UserManagerBase):
    pass


class User(AbstractUser):
    objects = UserManager()
