# TODOS models

from django.db import models
from django.conf import settings

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=30)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.name, self.color.name)

class Memo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)