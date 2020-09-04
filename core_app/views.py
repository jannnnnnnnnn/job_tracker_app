
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from bs4 import BeautifulSoup
import requests


def search(request):
    print(request)
    page = requests.get(
        "https://ca.indeed.com/jobs?q=Junior+Developer&l=Toronto%2C+ON")
    soup = BeautifulSoup(page.content, 'html5lib')
    alltitles = soup.find_all("h2", class_="title")
    print(alltitles)
    return render(request, 'search.html/', {'alltitles': alltitles})


def hello(request):
    return HttpResponse('hi')


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


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
