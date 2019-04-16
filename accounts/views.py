from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect('/admin')
    else:
        login_form = AuthenticationForm()
        return render(request, 'accounts/login.html', {
            'login_form': login_form,
        })


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save()
            auth_login(request, user)
            return redirect('todos:list')
    else:
        user_creation_form = UserCreationForm()
        return render(request, 'accounts/signup.html', {
            'user_creation_form': user_creation_form,
        })
