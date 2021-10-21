from django.urls import path , include
from .import views

app_name='blog'
urlpatterns = [
    
    path('', views.blog , name='blog'),
    path('add', views.add_blog , name='add_blog'),
    path('<int:id>', views.blog_details , name='blog_details'),
    
]