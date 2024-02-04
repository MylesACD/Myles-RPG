from django.shortcuts import render
from django.shortcuts import redirect
import random
from . import urls
# Create your views here.
def home(request):
    return render(request,"wiki/Ethos.html")

def get_random(request):
    return redirect(random.choice(get_articles()))

def get_articles():
    valid = []
    invalid = ["wiki-base","wiki-home","wiki-search-articles","wiki-random","WikiSettings",""]
    for url in urls.urlpatterns:
        if url.name not in invalid:
            valid.append(url.name)
    return valid
def search_articles(request):
    #if they have actually submitted something
    term  = request.POST["searched"]
    return render(request,"wiki-search-articles.html",{"searched":term})
    if request.method == "POST":
        "something"
    else:
        return render(request,"search-articles.html",{})