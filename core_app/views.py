from django.shortcuts import render
from django.http import HttpResponse
import requests
# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# def jobs_Index(request):
def jobresults(request):
    API = "https://cloud.google.com/jobs-api/"
    res = requests.get(API)
    data = res.json()
    print(data)
    return render(request, 'jobresults.html/')


def search(request):
    return render(request, 'search.html/')


def home(request):
    return HttpResponse('Hello')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html/', context)
