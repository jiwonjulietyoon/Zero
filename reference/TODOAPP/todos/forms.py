from django import forms
from .models import Label, Memo

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'color']

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content', 'label']
    
    def __init__(self, user, *args, **kwargs):
        super(MemoForm, self).__init__(*args, **kwargs)
        self.fields['label'].queryset = Label.objects.filter(user=user)