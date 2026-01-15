from django.shortcuts import render

def home(request):
    return render(request, 'app01/home.html')
