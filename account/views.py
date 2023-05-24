from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


# Create your views here.

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form .is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')

    return render(request, 'account/signup.html', {'form': form})


def login(request):

    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')

    return render(request, 'account/login.html')
