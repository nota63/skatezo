from django.shortcuts import render



def home(request):
    return render(request,'home/skatezo_development.html')