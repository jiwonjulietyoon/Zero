# ACCOUNTS views

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'accounts/forms.html', {
            'form': form,
        })
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:list')

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'accounts/forms.html', {
            'form': form,
        })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:list')


