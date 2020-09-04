from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def hello(request):
    return HttpResponse('hi')


def home(request):
  return render(request, 'home.html')

def search(request):
    return render(request, 'main_app/search.html')


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
