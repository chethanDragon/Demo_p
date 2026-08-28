from django.urls import path
from .views import *


urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('g/',g),
]