from django.shortcuts import render


# new branch 
def home(request):
    return render(request,'home/skatezo_development.html')