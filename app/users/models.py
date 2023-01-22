from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(default="default.jpg")
    
    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        
        
        #make sure the default image is enforced
        if not self.image or self.image == None or self.image == '':
            self.image = "default.jpg"
        img = Image.open(self.pfp.path)
            
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.pfp.path)
       