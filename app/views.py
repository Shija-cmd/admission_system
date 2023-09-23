from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DataForm
from . models import Data
from django.contrib import messages

@login_required
def index(request):
    shortlisted_applicants = Data.objects.all()
    context = {'shortlisted_applicants': shortlisted_applicants
    }
    return render(request, 'app/index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exist!")
            return redirect('register')
            
        if User.objects.filter(email = email):
            messages.error(request, "Email already exist!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "The usename must be Alpha-Numeric")
            return redirect('register')    
        
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect('login')
        
    return render(request, 'app/register.html', {})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        
        else:
            return HttpResponse('Error, user does not exist!')
        
    return render(request, 'app/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login')

def data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:    
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'app/data.html', context)


def base(request):
    return render(request, 'app/base.html', {})

def nav(request):
    return render(request, 'app/nav.html', {})

