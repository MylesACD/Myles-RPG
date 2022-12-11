from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(User,on_delete=models.PROTECT)
    level = models.IntegerField()
    image = models.ImageField(default="default.jpg",upload_to="character_art")
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, **kwargs):
        super().save(**kwargs)
        img = Image.open(self.image.path)
        
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Technique(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("technique-detail", kwargs={"pk": self.pk})
    
    
