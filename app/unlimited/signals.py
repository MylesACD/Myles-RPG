from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Character, Technique
from django.template.defaultfilters import slugify
import math

@receiver(pre_save, sender=Character)
def create_character_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

@receiver(post_save, sender=Character)
def update_technique_costs(sender, instance, *args, **kwargs):
    qset = Technique.objects.filter(character = instance)
    for tech in qset:
        tech.save()

@receiver(pre_save, sender=Character)
def set_character_points(sender, instance, *args, **kwargs):
    instance.point_pool = 10+ 2 * instance.level
    instance.current_points = 0
    qset = Technique.objects.filter(character = instance)
    for tech in qset:
        instance.current_points += tech.cost

  

@receiver(pre_save, sender=Technique)
def create_technique_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
        
@receiver(pre_save, sender=Technique)
def set_costs(sender, instance, *args, **kwargs):
    instance.max_cost = math.ceil(2 * (10+2*instance.character.level) / 3)
    instance.max_cost += 4*(instance.boon)
    instance.cost = int(instance.power)
    instance.cost -= int(instance.boon) * 4
    #----------tier 1 technique tags------------------
    instance.cost += 2* int(instance.multitarget)
    instance.cost += 2* int(instance.area) 
    instance.cost += 2* int(instance.range) 
    instance.cost += 2* int(instance.disarm)
    instance.cost += 2* int(instance.forceful) 
    #----------tier 2 technique tags------------------
    instance.cost += 3* int(instance.heal)
    instance.cost += 3* int(instance.destructive) 
    instance.cost += 3* int(instance.combo)
    instance.cost += 3* int(instance.immobilizing) 
    instance.cost += 3* int(instance.piercing)  
    instance.cost += 3* int(instance.controlled) 
    instance.cost += 3* int(instance.frightning) 
    instance.cost += 3* int(instance.cure) 
    instance.cost += 3* int(instance.mobile)
    #----------tier 3 technique tags------------------
    instance.cost += 4* int(instance.summon)
    instance.cost += 4* int(instance.vampiric) 
    instance.cost += 4* int(instance.practiced) 
    instance.cost += 4* int(instance.transformation)
    instance.cost += 4* int(instance.terrain) 
    instance.cost += 4* int(instance.armor_shred) 
    instance.cost += 4* int(instance.stunning) 
    instance.cost += 4* int(instance.subtle)
    
    # when saving cost of a technique update the points in use by the character 
    qset = Technique.objects.filter(character = instance.character)
    temp_total = 0
    for tech in qset:
        temp_total += tech.cost
    instance.character.update(current_points=temp_total)    
    
     