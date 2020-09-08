
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('landingpage/search/', views.search, name='search'),
    path('profile/search/', views.search, name='search'),
    path('savedjobs/search/', views.search, name='search'),
    path('searchpage/search/', views.search, name='search'),
    path('searchpage/', views.searchpage, name='searchpage'),
    path('profile/', views.profile, name='profile'),
    path('apptracker/', views.apptracker, name='apptracker'),
    path('profile_form/', views.ProfileCreate.as_view(), name='profile_create'),
    path('savedjobs/', views.savedjobs, name='savedjobs'),
    path('landingpage/', views.landingpage, name='landingpage'),
]
