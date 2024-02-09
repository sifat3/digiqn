from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserForm, UserProfileForm


@login_required(login_url='user_login')
def home(request):
    if request.method == 'POST':
        sender_name = request.POST['sender_name']
        sender_email = request.POST['sender_email']
        receiver_name = request.POST['receiver_name']
        receiver_email = request.POST['receiver_email']
        ammount = request.POST['ammount']
        service_description = request.POST['service_description']
        p_request = Request.objects.create(sender_email=sender_email, sender_name=sender_name, receiver_name=receiver_name, receiver_email=receiver_email, ammount=ammount, service_description=service_description)
        p_request.save()
        send_mail(f"PAYMENT REQUEST ID: {p_request.id}", f"Hello, {p_request.receiver_name}. You have pending payment request of {p_request.ammount} TAKA. Please visit this link - http://127.0.0.1:8000/request/{p_request.id} . Thank You.", 'digiqnfinance@gmail.com', [p_request.receiver_email])
        return redirect('home')
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
            send_mail(f"PAYMENT RECEIVED ID: {p_request.id}", f"Payment Received. Please Verify. Transaction ID: {p_request.transaction_id}. Ammount: {p_request.ammount} TAKA.", 'digiqnfinance@gmail.com', ['ahsifat321@gmail.com'])
            return redirect('request', pk)

    context = {"request": p_request}
    return render(request, "main/request.html", context)


def admin_area(request):
    requests = Request.objects.all()
    if request.method == 'POST':
        p_request = Request.objects.get(id = request.POST['id'])
        p_request.payment_done = True
        p_request.save()
        send_mail(f"PAYMENT RECEIVED ID: {p_request.id}", f"Hello, {p_request.sender_name}. We Received payment of {p_request.ammount} TAKA. Please share the service with the buyer. Thank You.", 'digiqnfinance@gmail.com', [p_request.sender_email])
        return redirect('admin_area')
    context = {
        'requests': requests
    }
    return render(request, 'main/admin.html', context)


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']

            # Create a CustomUser instance
            user = CustomUser.objects.create_user(email=email, password=password)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'main/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')  # Redirect to your home page
            else:
                return render(request, 'main/login.html', {'error_message': 'Your account is disabled.'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid login details.'})
    else:
        return render(request, 'main/login.html', {})
