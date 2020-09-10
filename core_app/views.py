
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Define the home view
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Industry, Skill, Savedjob
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SkillForm, IndustryForm, SavedjobForm, UserForm


def search(request):
    profile = Profile.objects.get(user=request.user)
    searchquery = request.GET.get('search_box')
    if searchquery:
        profile.searchquery = searchquery
        profile.save()
    else:
        searchquery = profile.searchquery
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

    listofjobs = []
    number = len(mergedtitleurl[0])-1

    for i in range(number):
        newjob = [mergedtitleurl[0][i], mergedtitleurl[1]
                  [i], mergedtitleurl[2][i], mergedtitleurl[3][i], "", False]
        listofjobs.append(newjob)

    # print(listofjobs[0])
    # print(listofjobs[10])
    savejob_forms = []
    for i in range(number):
        savejob_form = SavedjobForm(
            {'title': listofjobs[i][0], 'url': listofjobs[i][1], 'company': listofjobs[i][2], 'description': listofjobs[i][3]})
        listofjobs[i][4] = savejob_form
        savestatus = profile.savedjobs.filter(url=listofjobs[i][1]).count()
        if savestatus > 0:
            listofjobs[i][5] = True

    return render(request, 'main_app/search.html', {'mergedtitleurl': mergedtitleurl, 'range': range(30), 'savejob_forms': savejob_forms, 'listofjobs': listofjobs})


def save_job(request, user_id, job_id):
    Jobs.objects.get(id=user_id).jobs.save(job_id)
    return redirect('savedjobs', user_id=user_id)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    # skills_profile_doesnt_have = Skill.objects.exclude(
    #     id__in=profile.currentskill_set.all().values_list('id'))

    # We need skill template forms to be rendered in the template, and we need industry form to render in ProfileUpdate
    skill_form = SkillForm()
    user_form = UserForm()
    # industry_form=IndustryForm()

    return render(request, 'main_app/profile.html', {
        'profile': profile,
        'skill_form': skill_form,
        'user_form': user_form
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
    profile = Profile.objects.get(user=request.user)
    savedjobs = profile.savedjobs.all()
    print(savedjobs)
    return render(request, 'main_app/savedjobs.html', {'savedjobs': savedjobs})


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


def add_skill(request):
    print("i am in add_skill")
    form = SkillForm(request.POST)
    if form.is_valid():
        new_skill = form.save(commit=False)
        new_skill.save()
    profile = Profile.objects.get(user=request.user)
    this_skill = Skill.objects.get(id=new_skill.id)
    profile.skills.add(this_skill)
    return redirect('profile')


def savejob(request):
    print("i am in saving job function")
    form = SavedjobForm(request.POST)
    if form.is_valid():
        new_job = form.save(commit=False)
        new_job.save()
    profile = Profile.objects.get(user=request.user)
    this_job = Savedjob.objects.get(id=new_job.id)
    profile.savedjobs.add(this_job)
    return redirect('search')


class SkillDelete(DeleteView):
    model = Skill
    success_url = '/profile/'


class JobDelete(DeleteView):
    model = Savedjob
    success_url = '/savedjobs/'
