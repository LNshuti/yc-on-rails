# Start with installing the necessary packages (add these to your requirements.txt)
# django==3.2
# stripe==2.55.0

import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

import stripe

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
stripe.client_id = os.getenv("STRIPE_CLIENT_ID")

# In your views.py

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<a href="{url}">Connect with Stripe</a>'.format(url=reverse('authorize')))

class AuthorizeView(View):
    def get(self, request, *args, **kwargs):
        url = stripe.OAuth.authorize_url(scope="read_only")
        return HttpResponseRedirect(url)

class CallbackView(View):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        try:
            resp = stripe.OAuth.token(grant_type="authorization_code", code=code)
        except stripe.oauth_error.OAuthError as e:
            return HttpResponse("Error: " + str(e))
        return render(request, "callback.html", {'stripe_user_id': resp["stripe_user_id"]})

class DeauthorizeView(View):
    def get(self, request, *args, **kwargs):
        stripe_user_id = request.GET.get("stripe_user_id")
        try:
            stripe.OAuth.deauthorize(stripe_user_id=stripe_user_id)
        except stripe.oauth_error.OAuthError as e:
            return HttpResponse("Error: " + str(e))
        return render(request, "deauthorize.html", {'stripe_user_id': stripe_user_id})

# In your urls.py

from django.urls import path
from .views import IndexView, AuthorizeView, CallbackView, DeauthorizeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
    path('oauth/callback/', CallbackView.as_view(), name='callback'),
    path('deauthorize/', DeauthorizeView.as_view(), name='deauthorize'),
]
