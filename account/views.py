from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User

# Create your views here.

def login(request):
    if request.method ==  'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        # print(email, password)

        if password and email:
            user = authenticate(email=email, password=password)
           
            print(user)
            if user is not None:
                auth_login(request, user)
                # print('User', user)
                return redirect('/')
        

    return render(request,'frontendfiles/login.html')

def signup(request):
    if request.method == "POST":

        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if first_name and last_name and email and password:
            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
            return redirect('/login/')
            # print('User Created', user)
        else:
            print("Something went wrong")
    else:
        print('just hold am')

    return render(request, 'frontendfiles/signup.html')
