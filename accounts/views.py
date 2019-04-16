from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_POST

# Create your views here.

def login_signup(request):
    login_form = AuthenticationForm()
    user_creation_form = UserCreationForm()

    return render(request, 'accounts/login_signup.html', {
        'login_form': login_form,
        'user_creation_form': user_creation_form,
    })


@require_POST
def login(request):
    login_form = AuthenticationForm(request, request.POST)
    if login_form.is_valid():
        auth_login(request, login_form.get_user())
        return redirect('todos:list')


@require_POST
def signup(request):
    user_creation_form = UserCreationForm(request.POST)
    if user_creation_form.is_valid():
        user = user_creation_form.save()
        auth_login(request, user)
        return redirect('todos:list')


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')



