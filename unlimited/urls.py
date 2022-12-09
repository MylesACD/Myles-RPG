from django.urls import path
from . import views
from .views import TechniqueListView, TechniqueDetailView, TechniqueCreateView, TechniqueUpdateView, TechniqueDeleteView
urlpatterns =[
        path('',TechniqueListView.as_view(),name="unlimited-home"),
        path('about/',views.about,name="unlimited-about"),
        path('technique/<int:pk>/',TechniqueDetailView.as_view(),name="technique-detail"),
        path('technique/new/',TechniqueCreateView.as_view(),name="technique-create"),
        path('technique/<int:pk>/update/',TechniqueUpdateView.as_view(),name="technique-update"),
        path('technique/<int:pk>/delete/',TechniqueDeleteView.as_view(),name="technique-delete"),
    ]
