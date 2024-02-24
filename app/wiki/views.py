from collections import defaultdict
from typing import Any
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView
import random
import os
import string
from pathlib import Path
from . import urls
invalid = ["wiki-base","wiki-home","wiki-search-articles","wiki-random","WikiSettings",""]
# Create your views here.
def home(request):
    return render(request,"wiki/Ethos.html")

def get_random(request):
    return redirect(random.choice(get_articles()))

def get_articles():
    valid = []
    for url in urls.urlpatterns:
        if url.name not in invalid:
            valid.append(url.name)
    return valid


def get_relevant_articles(term):
    
    curr_dir =os.getcwd() + "/wiki/templates/wiki"
    counts = defaultdict(int)
    true_term = " "+term.lower()+" "
    term = term.lower()
    
    for file in os.scandir(curr_dir):
        with open(file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        name = file.name.split("/")[-1].split(".")[0]
        
        if name not in invalid:
            
            if true_term in file.name.lower():
                counts[name] += 1000
            elif term in file.name.lower():
                counts[name] += 100
                
            if html_content:
                counts[name] += html_content.lower().count(true_term)*10
                counts[name] += html_content.lower().count(term)
    
    
   
    counts = {k:v for (k,v) in counts.items() if v>0}
    return sorted(counts.items(),key=lambda item:item[1], reverse=True)
    

class SearchView(ListView):
    #if they have actually submitted something
    def post(self, request):    
            term =  request.POST.get("search")
            context = {"searched":term}
            context["articles"] = get_relevant_articles(term)
            return render(request,"wiki/wiki-search-articles.html",context)
 
    def get(self,request):
            return render(request,"wiki/wiki-search-articles.html")