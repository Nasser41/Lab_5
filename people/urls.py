from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_people, name='index'),
    path('add/', views.add_person, name='add'),
]
