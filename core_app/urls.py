
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('apptracker/', views.apptracker, name='apptracker'),
    path('profile_form/', views.ProfileCreate.as_view(), name='profile_form'),
    path('savedjobs/', views.savedjobs, name='savedjobs')
]
