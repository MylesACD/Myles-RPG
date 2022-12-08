from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Technique
# Create your views here.

def home(request):
    context ={
        "techniques": Technique.objects.all()
    }
    return render(request,"unlimited/home.html",context)

class TechniqueListView(ListView):
    model = Technique
    template_name = "unlimited/home.html"
    context_object_name = "techniques"
    ordering = ["-date_created"]
    
class TechniqueDetailView(DetailView):
    model = Technique
    
class TechniqueCreateView(CreateView):
    model = Technique    
    fields = ["name", "content"]
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TechniqueUpdateView(UpdateView):
    model = Technique    
    
class TechniqueDeleteView(DeleteView):
    model = Technique    
    
def about(request):
    return render(request,"unlimited/about.html")