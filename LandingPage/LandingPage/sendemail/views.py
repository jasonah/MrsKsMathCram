from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import EmailSignupForm
from .models import Signup
import json
import requests

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_AUDIENCE_ID = settings.MAILCHIMP_EMAIL_AUDIENCE_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_AUDIENCE_ID}/members'

def post_list(request):
    return render(request, 'sendemail/index.html')

def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed",
    }

    r = requests.post(
        members_endpoint,
        auth = ("", MAILCHIMP_API_KEY),
        data = json.dumps(data)
    )

    return r.status_code, r.json()

def email_list_signup(request):
    form = EmailSignupForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = Signup.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.info(request, "You are already signed up, Thanks!")
            else:
                subscribe(form.instance.email)
                messages.success(request, "Thank you for signing up. You will be emailed shortly! If the email does not show up in your inbox, please check \"spam\" or \"promotions\".")
                form.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def index(request):
    form = EmailSignupForm()
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)
