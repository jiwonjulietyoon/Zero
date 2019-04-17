from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Card(models.Model):
    title = models.CharField(default='', max_length=255)
    content = models.TextField(default='')
    image = models.ImageField(blank=True, upload_to='cards/media')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} // created_at:{self.created_at} // updated_at:{self.updated_at}"


class Label(TimeStampedModel):
    name = models.CharField(blank=True, max_length=50)
    color = models.IntegerField(default=1, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
