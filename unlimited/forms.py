from django import forms
from django.contrib.auth.models import User
from .models import Technique,Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from crispy_forms.bootstrap import Accordion, AccordionGroup


class TechniqueForm(forms.ModelForm):
    
    
    
    class Meta:
        model = Technique
        fields = ["character","name",
                  "multitarget","range","area","disarm","forceful",
                  "destructive","combo","heal","immobilizing","piercing","controlled","frightning","cure",
                  "vampiric","practiced","transformation","summon","armor_shred","terrain","stunning",
                  ]
        
        labels = {
            'armor_shred': 'Armor Shred',
            "terrain": "Create Terrain",
        }

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(TechniqueForm, self).__init__(*args, **kwargs)
       #user must own the character
       self.fields['character'].queryset = Character.objects.filter(player=user) 
          
       self.helper = FormHelper()
       self.helper.layout = Layout(
           Fieldset("","name","character"),
           Accordion(AccordionGroup("Tier 1 (2 points)","multitarget","area","range","disarm","forceful")),
           Accordion(AccordionGroup("Tier 2 (3 points)","destructive","combo","heal","immobilizing","piercing","controlled","frightning","cure")),
           Accordion(AccordionGroup("Tier 3 (4 points)","vampiric","practiced","transformation","summon","armor_shred","terrain","stunning")),
           Submit('submit', 'Done', css_class="btn btn-outline-info")
       )
       