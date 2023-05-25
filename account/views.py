from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm


# Create your views here.

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST' and request.user.is_authenticated is False:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'account/signup.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')
