
from django.urls import path
from . import views
import os
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns =[
        path('',views.home,name="wiki-home"),
        path("Classes.html",TemplateView.as_view(template_name="wiki/Classes.html"), name="class"),
        path("random", views.get_random, name='wiki-random'),
    ]

dir = os.path.join(os.getcwd(),"wiki/templates/wiki")
file_list = os.listdir(dir)
for file in file_list:
    name = file.replace('.html', '')
    route = path(file, TemplateView.as_view(template_name=os.path.join("wiki/",file)), name=name)
    urlpatterns.append(route)

