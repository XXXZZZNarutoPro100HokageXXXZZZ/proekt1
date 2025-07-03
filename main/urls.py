from .import views
from django.urls import path

urlpatterns = [
 path('', views.index, name='Мой блог'),
 path('about', views.about, name='О себе'),
 path('nier', views.nier, name='nier'),
 path('persona', views.persona, name='persona'),
 path('bmw', views.bmw, name='bmw'),
 path('create', views.create, name='create'),

]