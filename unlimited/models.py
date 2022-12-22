from argparse import _ArgumentGroup
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.template.defaultfilters import slugify
from django import forms
# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=100,unique=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(User,on_delete=models.PROTECT)
    level = models.IntegerField()
    image = models.ImageField(default="default.jpg",upload_to="character_art",blank=True)
    slug = models.SlugField(null=True,unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args ,**kwargs):
        img = Image.open(self.image.path)
        
        if not self.slug:
            self.slug = slugify(self.name)
        
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
        return  super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("character-detail", kwargs={"slug": self.slug})


class Technique(models.Model):
    #----------tier 1 technique tags------------------
    MULTITARGET_CHOICES = (("1","1"),("2","2"),("3","3"),("4","4"))
    AREA_CHOICES = (("none","none"),("small","small"),("medium","medium"),("large","large"))
    RANGE_CHOICES = (("touch","touch"),("reach","reach"),("near","near"),("far","far"),("remote","remote"))
   
    multitarget = models.CharField(default="1",max_length=100,choices=MULTITARGET_CHOICES)
    area = models.CharField(default="none",max_length=100,choices=AREA_CHOICES) 
    range = models.CharField(default="touch",max_length=100,choices=RANGE_CHOICES)
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
    #----------tier 3 technique tags------------------
    SUMMON_CHOICES =  (("0","0"),("1","1"),("2","2"),("3","3"))
    
    summon = models.CharField(default="0",max_length=100,choices=SUMMON_CHOICES)
    vampiric = models.BooleanField(default=False)
    practiced = models.BooleanField(default=False)
    transformation = models.BooleanField(default=False)
    stunning = models.BooleanField(default=False)
    #these 2 get labels
    armor_shred = models.BooleanField(default=False)
    terrain = models.BooleanField(default=False)
    
    
    
    name = models.CharField(max_length=100,unique=True)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    slug = models.SlugField(null=True,unique=True)
    
   
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("technique-detail", kwargs={"slug": self.slug})
    
    
    def save(self,*args ,**kwargs):
        
        if not self.slug:
            self.slug = slugify(self.name)
        
        return  super().save(*args,**kwargs)
    
