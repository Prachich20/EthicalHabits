from django.shortcuts import render
import ethics.settings as settings


def index(request):
    return render(request, 'sms/home.html')
