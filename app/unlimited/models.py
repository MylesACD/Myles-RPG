from argparse import _ArgumentGroup
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.template.defaultfilters import slugify
from django import forms
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib import messages
# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100,unique=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(User,on_delete=models.CASCADE)
    level = models.IntegerField()
    image = models.ImageField(default="default.jpg",blank=True)
    slug = models.SlugField(null=True,unique=True)
    current_points = models.IntegerField(null=True)
    point_pool = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args ,**kwargs):
        super().save(*args,**kwargs)
        
        if not self.slug:
            self.slug = slugify(self.name)
        
        try:
            img = Image.open(self.image.path)
            if img.height>300 or img.width>300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)  
        except:
            pass
        
        return super().save(*args,**kwargs)
    
    
    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"slug": self.slug})


          


class Technique(models.Model):
    
    #----------tier 0 technique tags------------------
    power = models.IntegerField(default=0,null=True)
    boon = models.BooleanField(default=False)
    #----------tier 1 technique tags------------------
    MULTITARGET_CHOICES = (("0","1"),("1","2"),("2","3"),("3","4"))
    AREA_CHOICES = (("0","none"),("1","small"),("2","medium"),("3","large"),("4","huge"),("5","enormous"),("6","colossal"),("7","titanic"))
    RANGE_CHOICES = (("0","close"),("1","reach"),("2","near"),("3","far"),("4","remote"))
   
    multitarget = models.CharField(default="0",max_length=100,choices=MULTITARGET_CHOICES, )
    area = models.CharField(default="0",max_length=100,choices=AREA_CHOICES) 
    range = models.CharField(default="0",max_length=100,choices=RANGE_CHOICES)
    disarm = models.BooleanField(default=False)
    forceful = models.BooleanField(default=False)
    #----------tier 2 technique tags------------------
    HEAL_CHOICES = (("0","0%"),("1","50%"),("2","100%"))
    
    heal = models.CharField(default="0",max_length=100,choices=HEAL_CHOICES)
    destructive = models.BooleanField(default=False)
    combo = models.BooleanField(default=False)
    immobilizing = models.BooleanField(default=False)
    piercing = models.BooleanField(default=False)
    controlled = models.BooleanField(default=False)
    frightning = models.BooleanField(default=False)
    cure = models.BooleanField(default=False)
    mobile = models.BooleanField(default=False,null=True)
    #----------tier 3 technique tags------------------
    SUMMON_CHOICES =  (("0","None"),("1","1"),("2","2"),("3","3"))
    
    summon = models.CharField(default="0",max_length=100,choices=SUMMON_CHOICES)
    vampiric = models.BooleanField(default=False)
    practiced = models.BooleanField(default=False)
    transformation = models.BooleanField(default=False)
    stunning = models.BooleanField(default=False)
    subtle = models.BooleanField(default=False,null=True)
    #these 2 get labels
    armor_shred = models.BooleanField(default=False)
    terrain = models.BooleanField(default=False)
    
    name = models.CharField(max_length=100,unique=True)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, null=True,on_delete=models.SET_NULL)
    slug = models.SlugField(null=True,unique=True)
    
    max_cost = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)
   
   
    success_message = "Technique saved successfully"
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("technique-update", kwargs={"slug": self.slug})
    
    
    def save(self,*args ,**kwargs):
        return  super().save(*args,**kwargs)
    
    def get_success_message(self):
        return self.success_message
    
    