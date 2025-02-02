from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdminBase

from .forms import UserCreationForm, UserChangeForm

# from .models import User

User = get_user_model()


class UserAdmin(UserAdminBase):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm


admin.site.register(User, UserAdmin)
