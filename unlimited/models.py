from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Technique(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("technique-detail", kwargs={"pk": self.pk})
    
    