from django.urls import path
from . import views
from .views import TechniqueListView, TechniqueDetailView, TechniqueCreateView, TechniqueUpdateView, TechniqueDeleteView, UserTechniqueListView 
from .views import CharacterCreateView,CharacterDeleteView, CharacterUpdateView, CharacterDetailView
urlpatterns =[
        path('',TechniqueListView.as_view(),name="unlimited-home"),
        path('technique/new/',TechniqueCreateView.as_view(),name="technique-create"),
        path('about/',views.about,name="unlimited-about"),
        path('technique/<slug:slug>/',TechniqueDetailView.as_view(),name="technique-detail"),
        path('technique/<slug:slug>/update/',TechniqueUpdateView.as_view(),name="technique-update"),
        path('technique/<slug:slug>/delete/',TechniqueDeleteView.as_view(),name="technique-delete"),
        path('user/<str:username>',UserTechniqueListView.as_view(), name="user-techniques"),
        path('character/new/',CharacterCreateView.as_view(),name="character-create"),
        path('character/<slug:slug>/',CharacterDetailView.as_view(),name="character-detail"),
        path('character/<slug:slug>/update/',CharacterUpdateView.as_view(),name="character-update"),
        path('character/<slug:slug>/delete/',CharacterDeleteView.as_view(),name="character-delete"),
        
    ]
