
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):


    return render(request,'home.html')
def g(request):
    about='hii i am chethan i have completed my groduation in davangere'
    return HttpResponse(about)

def about(request):

    return render(request,'about.html')

def login(request):

    return render(request,'login.html')

def logout(request):

    return render(request,'logout.html')

