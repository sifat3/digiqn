from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def wwd(request):
    return render(request, 'main/whatwedo.html')


def contactus(request):
    return render(request, 'main/contactus.html')