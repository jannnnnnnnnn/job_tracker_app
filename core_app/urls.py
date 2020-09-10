
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('landingpage/search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('apptracker/', views.apptracker, name='apptracker'),
    path('profile_form/', views.ProfileCreate.as_view(), name='profile_create'),
    path('savedjobs/', views.savedjobs, name='savedjobs'),
    path('landingpage/search/savejob', views.savejob, name='savejob'),

    path('landingpage/', views.landingpage, name='landingpage'),
    path('profile/<int:pk>/update/',
         views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/add_skill/', views.add_skill, name='add_skill'),

]
