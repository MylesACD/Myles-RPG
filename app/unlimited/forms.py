from django import forms
from django.contrib.auth.models import User
from .models import Technique,Character
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, BaseInput, Button, ButtonHolder
from crispy_forms.bootstrap import Accordion, AccordionGroup

class TechniqueForm(forms.ModelForm):
        
    class Meta:
        model = Technique
        fields = ["character","name",
                  "power", "boon",
                  "multitarget","range","area","disarm","forceful",
                  "destructive","combo","heal","restricting","piercing","controlled","frightening","lasting", "mobile",
                  "vampiric","practiced","transformation","summon","terrain","stunning", "subtle",
                  ]
        
        labels = {
            "boon": "Boon/Bane",
            "terrain": "Create Terrain",
            "power": "Power (+damage)",
        }

    def __init__(self, *args, **kwargs):
       
        user = kwargs.pop('user')
        super(TechniqueForm, self).__init__(*args, **kwargs)
        tech = self.instance
        
        #user must own the character
        self.fields['character'].queryset = Character.objects.filter(player=user) 
        self.fields["power"].required = False
        self.fields["multitarget"].required = False
        self.fields["area"].required = False
        self.fields["range"].required = False
        self.fields["heal"].required = False
        self.fields["summon"].required = False
        self.fields["forceful"].required = False
        self.fields["piercing"].required = False
          
        self.helper = FormHelper()
        self.helper.layout = Layout(
           Accordion(AccordionGroup("Info","name","character")),
           Accordion(AccordionGroup("Tier 0","power","boon")),
           Accordion(AccordionGroup("Tier 1 (2 points)","disarm","forceful","multitarget","range")),
           Accordion(AccordionGroup("Tier 2 (3 points)","destructive","combo","heal","restricting","piercing","controlled","frightening","lasting","mobile")),
           Accordion(AccordionGroup("Tier 3 (4 points)","area","vampiric","practiced","transformation","summon","terrain","stunning", "subtle")),
           ButtonHolder(
               Submit('submit', 'Submit', css_class="btn btn-outline-info"),
           ),
        )

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields=["name","level","image",]
        widgets = {
            'image': forms.FileInput
        }
    
    def __init__(self,*args,**kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset("Create A Character","name","level","image"),
            Submit('submit', 'Done', css_class="btn btn-outline-info"),
        )