from django.shortcuts import render
from django.shortcuts import redirect
import random
from . import urls
# Create your views here.
def home(request):
    return render(request,"wiki/Ethos.html")

def get_random(request):
    response = redirect(random.choice(urls.urlpatterns).name)
    return response
    