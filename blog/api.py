from .models import Blog
from . Serializers import BlogSerializer
from rest_framework import generics


class Blog_List(generics.ListCreateAPIView):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer
 

class Blog_Detail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer
   lookup_field = 'id'
 

