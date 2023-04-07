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
    level = models.PositiveIntegerField(default=1)
    image = models.ImageField(default="default.jpg",blank=True)
    slug = models.SlugField(null=True,unique=True)
    
    current_points = models.IntegerField(null=True)
    point_pool = models.IntegerField(null=True)
    max_cost = models.IntegerField(null=True)
    available_points = models.IntegerField(null=True, default = 0)
    
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
    power = models.PositiveIntegerField(default=0,null=True)
    boon = models.BooleanField(default=False)
    #----------tier 1 technique tags------------------
    MULTITARGET_CHOICES = (("0","1"),("1","2"),("2","3"),("3","4"))
    RANGE_CHOICES = (("0","close"),("1","reach"),("2","near"),("3","far"),("4","remote"))
   
    multitarget = models.CharField(default="0",max_length=100,choices=MULTITARGET_CHOICES, )
    range = models.CharField(default="0",max_length=100,choices=RANGE_CHOICES)
    disarm = models.BooleanField(default=False)
    forceful = models.PositiveIntegerField(default=0)
    #----------tier 2 technique tags------------------
    HEAL_CHOICES = (("0","0%"),("1","50%"),("2","100%"))
    
    heal = models.CharField(default="0",max_length=100,choices=HEAL_CHOICES)
    destructive = models.BooleanField(default=False)
    combo = models.BooleanField(default=False)
    restricting = models.BooleanField(default=False)
    piercing = models.BooleanField(default=False)
    controlled = models.BooleanField(default=False)
    frightening = models.BooleanField(default=False)
    mobile = models.BooleanField(default=False)
    lasting = models.BooleanField(default=False)
    #----------tier 3 technique tags------------------
    SUMMON_CHOICES =  (("0","None"),("1","1"),("2","2"),("3","3"))
    AREA_CHOICES = (("0","none"),("1","small"),("2","medium"),("3","large"),("4","huge"),("5","enormous"),("6","colossal"),("7","titanic"))
    
    area = models.CharField(default="0",max_length=100,choices=AREA_CHOICES) 
    summon = models.CharField(default="0",max_length=100,choices=SUMMON_CHOICES)
    vampiric = models.BooleanField(default=False)
    practiced = models.BooleanField(default=False)
    transformation = models.BooleanField(default=False)
    stunning = models.BooleanField(default=False)
    subtle = models.BooleanField(default=False)
    #these 2 get labels
    terrain = models.BooleanField(default=False)
    
    name = models.CharField(max_length=100,unique=True)
    content = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, null=True,on_delete=models.SET_NULL)
    slug = models.SlugField(null=True,unique=True)
    public = models.BooleanField(default=False,null=True)
    
    cost = models.IntegerField(null=True)
    max_cost = models.IntegerField(default= 0)
    
   
   
    success_message = "Technique saved successfully"
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("technique-update", kwargs={"slug": self.slug})
    
    
    def save(self,*args ,**kwargs):
        return  super().save(*args,**kwargs)
    
    def get_success_message(self):
        return self.success_message
    
    def toggle_public(self):
        self.public = not self.public
        self.save()
    
    def active_tags(self):
        """
        Returns a list of a model's fields that are not the default value.
        """
        nondefault_fields = []
        # TODO maybe find a way to automate these lists
        exempt_field_names = ["id","name","last_modified","date_created","author","character","slug","cost","max_cost","public"]
        tier1 = ["disarm","forceful","range","multitarget"]
        tier2 = ["heal","destructive","combo","restricting","piercing","controlled","frightning","lasting","mobile"]
        tier3 = ["area","vampiric","practiced","transformation","summon","terrain","stunning","subtle"]

        # Loop through all the fields of the model
        for field in self._meta.fields:

            # Get the value of the field for the model instance
            field_value = getattr(self, field.name)
            
            # Compare the field's value with the default value
            if field_value != field.get_default() and field.name not in exempt_field_names:
                
                if field.name == "power":
                    cost = int(field_value)
                elif field.name == "boon":
                    cost = -4
                elif field.name in tier1:
                    cost = 2 * int(field_value)
                elif field.name in tier2:
                    cost = 3 * int(field_value)
                else:
                    cost = 4 * int(field_value)
                
                label = field.name
                # only add the value if the field is not a boolean field
                if str(field_value) != "True":
                     label+= ": " + str(field_value)

                    
                nondefault_fields.append((cost,label))

        return nondefault_fields
    