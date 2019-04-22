# TODOS views

from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo, Label
from .forms import LabelForm, MemoForm

# Create your views here.
def list(request):
    if request.user.is_authenticated:
        memos = Memo.objects.all().filter(user=request.user)
        return render(request, 'todos/list.html', {
            'memos': memos,
        })
    else:
        return redirect('accounts:login')


def create_memo(request):
    if request.method == "GET":
        memo_form = MemoForm(request.user)
        return render(request, 'todos/forms.html', {
            'form': memo_form,
        })
    else:
        form = MemoForm(request.user, request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.user = request.user
            memo.save()
            return redirect('todos:list')
    
def create_label(request):
    if request.method == "GET":
        label_form = LabelForm()
        return render(request, 'todos/forms.html', {
            'form': label_form,
        })
    else:
        form = LabelForm(request.POST)
        if form.is_valid():
            label = form.save(commit=False)
            label.user = request.user
            label.save()
            return redirect('todos:list')

def labels(request):
    labels = Label.objects.filter(user=request.user)
    return render(request, 'todos/all_labels.html', {
        'labels': labels,
    })

def edit_label(request, label_id):
    label = get_object_or_404(Label, pk=label_id)
    if request.method == "GET":
        label_form = LabelForm(instance=label)
        return render(request, 'todos/forms.html', {
            'form': label_form,
        })
    else:
        label_form = LabelForm(request.POST, instance=label)
        if label_form.is_valid():
            label_form.save()
            return redirect('todos:labels')


