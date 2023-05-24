from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# Create your views here.

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form .is_valid():
            form.save()

    return render(request, 'account/signup.html', {'form': form})


def login(request):
    return render(request, 'account/login.html')
