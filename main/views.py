from django.shortcuts import render, redirect
from .models import *


def home(request):
    return render(request, 'main/home.html')


def wwd(request):
    return render(request, 'main/whatwedo.html')


def contactus(request):
    return render(request, 'main/contactus.html')


def request_page(request, pk):
    p_request = Request.objects.get(id=pk)

    if request.method == 'POST':
        if request.POST['transaction_id'] == '':
            p_request.service_done = True
            p_request.save()
            return redirect('request', pk)
        else:
            p_request.transaction_id = request.POST['transaction_id']
            p_request.save()
            return redirect('request', pk)

    context = {"request": p_request}
    return render(request, "main/request.html", context)

