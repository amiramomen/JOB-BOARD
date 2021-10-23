from django.urls import path , include
from .import views
from .import api

app_name='blog'
urlpatterns = [
    
    path('', views.blog , name='blog'),
    path('add', views.add_blog , name='add_blog'),
    path('<int:id>', views.blog_details , name='blog_details'),
    
    #api 
    path('api/blogs', api.Blog_List.as_view() , name='Blog_List'),
    path('api/blogs/<int:id>', api.Blog_Detail.as_view() , name='Blog_Detail'),


]