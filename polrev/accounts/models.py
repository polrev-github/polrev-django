from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as UserManagerBase

from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class UserManager(UserManagerBase):
    pass

class User(AbstractUser):
    objects = UserManager()
    
'''
class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # This isn't tested, but should work
        try:
            user = User.objects.get(email=sociallogin.email_addresses[0])
            sociallogin.connect(request, user)
            # Create a response object
            raise ImmediateHttpResponse(response)
        except User.DoesNotExist:
            pass
'''