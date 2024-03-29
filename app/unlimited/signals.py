from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Character, Technique
from django.template.defaultfilters import slugify
import math

@receiver(pre_save, sender=Character)
def create_character_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
    
@receiver(pre_save,sender=Character)
def set_character_properties(sender, instance,*args,**kwargs):
    instance.point_pool = 12+ 3 * instance.level
    instance.current_points = 0
    instance.max_cost = math.ceil(2 * (instance.point_pool) / 3)    
    instance.available_points = 0
    
    for tech in Technique.objects.filter(character = instance):
        
        # dont add technique cost if boon brings it below 0
        if tech.cost > 0:
            instance.current_points += tech.cost
        
            
    instance.available_points = instance.point_pool - instance.current_points


  

@receiver(pre_save, sender=Technique)
def create_technique_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
        
@receiver(pre_save, sender=Technique)
def set_costs(sender, instance, *args, **kwargs):
    
    instance.max_cost = instance.character.max_cost
    instance.max_cost += 4*int(instance.boon)
    
    instance.cost = int(instance.power)
    instance.cost -= int(instance.boon) * 4
    #----------tier 1 technique tags------------------
    instance.cost += 2* int(instance.multitarget)
    instance.cost += 2* int(instance.range) 
    instance.cost += 2* int(instance.disarm)
    instance.cost += 2* int(instance.forceful) 
    #----------tier 2 technique tags------------------
    instance.cost += 3* int(instance.heal)
    instance.cost += 3* int(instance.destructive) 
    instance.cost += 3* int(instance.combo)
    instance.cost += 3* int(instance.restricting) 
    instance.cost += 3* int(instance.piercing)  
    instance.cost += 3* int(instance.controlled) 
    instance.cost += 3* int(instance.frightening) 
    instance.cost += 3* int(instance.mobile)
    instance.cost += 3* int(instance.lasting)
    #----------tier 3 technique tags------------------
    instance.cost += 4* int(instance.area) 
    instance.cost += 4* int(instance.summon)
    instance.cost += 4* int(instance.vampiric) 
    instance.cost += 4* int(instance.practiced) 
    instance.cost += 4* int(instance.transformation)
    instance.cost += 4* int(instance.terrain) 
    instance.cost += 4* int(instance.stunning) 
    instance.cost += 4* int(instance.subtle)
    
    instance.cost += int(instance.adjustment)
    # when saving cost of a technique update the points in use by the character 
    
        
@receiver(post_save, sender=Technique)
def save_character(sender, instance, *args, **kwargs):
    instance.character.save()

    