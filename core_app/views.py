
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Industry, Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SkillForm, IndustryForm, SavedjobForm


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
    if not htmltext:
        return render(request, 'main_app/error.html/')
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


def save_job(request, user_id, job_id):
    Jobs.objects.get(id=user_id).jobs.save(job_id)
    return redirect('savedjobs', user_id=user_id)


def home(request):
    return render(request, 'home.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    # skills_profile_doesnt_have = Skill.objects.exclude(
    #     id__in=profile.currentskill_set.all().values_list('id'))

    # We need skill template forms to be rendered in the template, and we need industry form to render in ProfileUpdate
    # skill_form = SkillForm()
    # industry_form=IndustryForm()

    return render(request, 'main_app/profile.html', {
        'profile': profile,
        # '_form': skill_form,
        # 'skills': skills_profile_doesnt_have
    })


def apptracker(request):
    return render(request, 'main_app/apptracker.html')


def searchpage(request):
    return render(request, 'main_app/landingpage.html')


def landingpage(request):
    return render(request, 'main_app/landingpage.html')


def profile_create(request):
    return render(request, 'core_app/profile_form.html')


def savedjobs(request):
    return render(request, 'main_app/savedjobs.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_create')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html/', context)


class ProfileCreate(CreateView):
    model = Profile
    fields = ['phone', 'city', 'gender', 'zipcode']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/profile/'


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['phone', 'city', 'zipcode']
    success_url = '/profile/'


def add_skill(request, user):
    form = SkillForm(request.POST)
    skill_form = SkillForm()
    if form.is_valid():
        new_skill = form.save(commit=False)
        new_skill.user = user
        new_skill.save()
    return redirect('profile/', user=user)
