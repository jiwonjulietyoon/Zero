from django.shortcuts import render, redirect
from .forms import CardModelForm, LabelModelForm
from .models import Card, Label
from IPython import embed

# Create your views here.

def list(request):
    if request.user.is_authenticated:   # 로그인된 유저만 메인 페이지로 이동
        return render(request, 'todos/list.html')
    else: # 로그인 안 된 사용자는 로그인 페이지로 이동
        return redirect('accounts:login_signup')


def create(request):
    if request.method == 'POST':
        pass
    else:
        card_model_form = CardModelForm()
        label_model_form = LabelModelForm()
        return render(request, 'todos/create.html', {
            'card_model_form': card_model_form,
            'label_model_form': label_model_form,
        })