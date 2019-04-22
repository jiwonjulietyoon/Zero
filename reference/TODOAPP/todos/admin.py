from django.contrib import admin
from .models import Color, Label, Memo

# Register your models here.
admin.site.register(Color)
admin.site.register(Label)
admin.site.register(Memo)