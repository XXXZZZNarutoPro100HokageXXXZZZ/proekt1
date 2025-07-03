from .import views
from django.urls import path

urlpatterns = [
 path('', views.news_home, name='news_home'),
 path('<int:pk>/', views.news_detail, name='news_detail'),
 path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
 path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]
