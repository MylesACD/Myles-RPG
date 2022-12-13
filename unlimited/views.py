from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Technique, Character
from django import forms
# Create your views here.

def home(request):
    context ={
        "techniques": Technique.objects.all()
    }
    return render(request,"unlimited/home.html",context)

    
def about(request):
    return render(request,"unlimited/about.html")

'''
Technique Views
'''
class TechniqueListView(ListView):
    model = Technique
    template_name = "unlimited/home.html"
    context_object_name = "techniques"
    ordering = ["-date_created"]
    paginate_by = 4
    
class UserTechniqueListView(ListView):
    model = Technique
    template_name = "unlimited/user_techniques.html"
    context_object_name = "techniques"
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Technique.objects.filter(author=user).order_by("-date_created")
        
class TechniqueDetailView(DetailView):
    model = Technique
          
class TechniqueForm(forms.ModelForm):
    class Meta:
       model = Technique
       choices = forms.MultipleChoiceField( widget  = forms.CheckboxSelectMultiple,)
       fields = ["name", "character","content"]

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(TechniqueForm, self).__init__(*args, **kwargs)
       self.fields['character'].queryset = Character.objects.filter(player=user)          
        
class TechniqueCreateView(LoginRequiredMixin, CreateView):
    model = Technique    
    form_class = TechniqueForm

    def get_form_kwargs(self):
        kwargs = super(TechniqueCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
    
class TechniqueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Technique    
    form_class = Technique
    
    def get_form_kwargs(self):
        kwargs = super(TechniqueCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        tech = self.get_object()
        return tech.author == self.request.user
    
class TechniqueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Technique    
    success_url = "/unlimited/"
    def test_func(self):
        tech = self.get_object()
        return tech.author == self.request.user 
      
'''
Character Views
'''
class CharacterCreateView(LoginRequiredMixin,CreateView):
    model = Character
    fields = ["name","level","image"]
    
    def form_valid(self,form):
        form.instance.player = self.request.user
        return super().form_valid(form)
    
class CharacterDetailView(DetailView):
    model = Character      
    
class CharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character    
    fields = ["name", "level", "image"]
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        character = self.get_object()
        return character.player == self.request.user
    
class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Character    
    success_url = "/unlimited/"
    def test_func(self):
        character = self.get_object()
        return character.player == self.request.user 