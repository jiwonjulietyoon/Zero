from django.shortcuts import render, redirect
from IPython import embed

# Create your views here.

def list(request):
    if request.user.is_authenticated:   # 로그인된 유저만 메인 페이지로 이동
        return render(request, 'todos/list.html')
    else: # 로그인 안 된 사용자는 로그인 페이지로 이동
        return redirect('accounts:login_signup')

