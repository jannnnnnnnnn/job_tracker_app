
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


def search(request):
    print('hello123')
    searchquery = request.GET.get('search_box')
    print(searchquery)
    url = f"https://www.simplyhired.ca/search?q={searchquery}&l=Toronto"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    htmltext = soup.find(
        "h2", class_="jobposting-title")
    htmlTextAll = soup.find_all(
        "h2", class_="jobposting-title")
    htmlatags = htmltext.find('a').get_text()
    htmlalinks = htmltext.find('a')
    joblinks = htmlalinks['href']
    joburl = 'simplyhired.ca' + joblinks
    alltitles = htmlatags
    allJobTitles = {
        "title": [],
        "url": [],
        "company": [],
        "snippet": []
    }

    for row in htmlTextAll:
        p = row.find('a')
        title = p.get_text()
        link = p['href']
        allJobTitles["title"].append(title)
        allJobTitles["url"].append('https://www.simplyhired.ca' + link)
        mergedtitleurl = (allJobTitles["title"], allJobTitles["url"])

    htmlTextAllSub = soup.find_all(
        "h3", class_="jobposting-subtitle")
    for row in htmlTextAllSub:
        company = row.get_text()
        allJobTitles["company"].append(company)
        mergedtitleurl = (
            allJobTitles["title"], allJobTitles["url"], allJobTitles["company"])

    htmlTextAllSnip = soup.find_all(
        "p", class_="jobposting-snippet")
    for row in htmlTextAllSnip:
        snippet = row.get_text()
        allJobTitles["snippet"].append(snippet)
        mergedtitleurl = (
            allJobTitles["title"], allJobTitles["url"], allJobTitles["company"], allJobTitles["snippet"])
    return render(request, 'main_app/search.html', {'mergedtitleurl': mergedtitleurl, 'range': range(30)})


# def save_job(request, user_id, job_id):
#   Jobs.objects.get(id=user_id).jobs.save(job_id)
#   return redirect('detail', user_id=user_id)


def hello(request):
    return HttpResponse('hi')


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def apptracker(request):
    return render(request, 'apptracker.html')


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
