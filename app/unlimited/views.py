from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Technique, Character
from .forms import TechniqueForm, CharacterForm
# Create your views here.

pagination= 4

# I forgot that is simple version of home is not even being used so changing does nothing
def home(request):
    context ={}
    return render(request,"unlimited/home.html",context)

    
def about(request):
    return render(request,"unlimited/about.html")

'''
Technique Views
'''
class TechniquePublicView(DetailView):
    model = Technique
    template_name = "unlimited/technique_publicity.html"

class TechniqueListView(ListView):
    model = Technique
    template_name = "unlimited/home.html"
    context_object_name = "techniques"
    ordering = ["-date_created"]
    paginate_by = pagination
    
    def get_queryset(self):
        current_user = self.request.user
        # some redudant checks just to make sure
        # if the logged in user is a super user show all techiniques
        if current_user and current_user.is_authenticated and current_user.is_superuser:
            return Technique.objects.order_by("-date_created")
        else:
            return Technique.objects.filter(public=True).order_by("-date_created")
        
    def get_paginate_by(self,queryset):
        return self.request.GET.get("paginate_by",self.paginate_by)
    
class UserTechniqueListView(ListView):
    model = Technique
    template_name = "unlimited/user_techniques.html"
    context_object_name = "techniques"
    paginate_by = pagination
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        current_user = self.request.user
       
        # if the logged in user is a super user or the user in question show all their techiniques
        if current_user.is_superuser or current_user is user:
            return Technique.objects.filter(author=user).order_by("-date_created")
        else:
            return Technique.objects.filter(public=True).filter(author=user).order_by("-date_created")
        
class TechniqueDetailView(DetailView):
    model = Technique       

          
#TODO this class and TechniqueUpdateView are basiaclly the same thing
#maybe find a way to combine the code for future simplicity 
class TechniqueCreateView(LoginRequiredMixin, CreateView,SuccessMessageMixin):
    model = Technique    
    form_class = TechniqueForm
    
    success_message = "Technique saved successfully"
    
    def get_form_kwargs(self):
        kwargs = super(TechniqueCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
    
class TechniqueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView,SuccessMessageMixin):
    model = Technique    
    form_class = TechniqueForm
    success_message = "Technique saved successfully"
    def get_form_kwargs(self):
        kwargs = super(TechniqueUpdateView, self).get_form_kwargs()
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
    form_class = CharacterForm
    
    def form_valid(self,form):
        form.instance.player = self.request.user
        return super().form_valid(form)
    
class CharacterDetailView(DetailView):
    model = Character      
    
class CharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character
    form_class = CharacterForm    
    
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