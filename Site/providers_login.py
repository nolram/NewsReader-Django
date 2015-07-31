__author__ = 'nolram'

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterProvider
from rest_auth.registration.views import SocialLogin


class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLogin):
    adapter_class = TwitterProvider
