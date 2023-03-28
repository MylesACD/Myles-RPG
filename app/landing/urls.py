from django.urls import path
from . import views
urlpatterns =[
    path('',views.landing,name="landing"),
    path('roll', views.roll, name="roll"),
    ]
