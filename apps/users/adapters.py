from allauth import app_settings
from allauth.account.utils import perform_login
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver

from apps.users.models import User


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            customer = User.objects.get(
                email=user.email)  # if user exists, connect the account to the existing account and login
            sociallogin.state['process'] = 'connect'
            perform_login(request, customer, 'none')
        except User.DoesNotExist:
            pass

# @receiver(pre_social_login)
# def link_to_local_user(sender, request, sociallogin, **kwargs):
#     import pdb
#     pdb.set_trace()
#     email_address = sociallogin.account.extra_data['email']
#     users = User.objects.filter(email=email_address)
#     if users:
#         perform_login(request, users[0], email_verification=app_settings.EMAIL_VERIFICATION)
