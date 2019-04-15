from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(default='', max_length=255)
    content = models.TextField(default='')
    image = models.ImageField(blank=True, upload_to='cards/media')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} // created_at:{self.created_at} // updated_at:{self.updated_at}"