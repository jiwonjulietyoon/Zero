from django import forms
from .models import Card, Label

class CardModelForm(forms.ModelForm):
    title = forms.CharField(label='제목', max_length=255, widget=forms.Textarea(attrs={
        'placeholder': '제목을 입력하세요.',
    }))
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'placeholder': '내용을 입력하세요',
    }))
    class Meta:
        model = Card
        fields = ['title', 'content', 'image']


class LabelModelForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    class Meta:
        model = Label
        fields = ['name', 'color']
        widgets = {
            'color': forms.Select(),
        }
