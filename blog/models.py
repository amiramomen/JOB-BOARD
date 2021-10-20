from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import Profile
# Create your models here.
Blog_Type = (
('travel','travel'),
('love','love'),
('life-style','life-style'),
('technology','technology'),
('illustration','illustration'),
('design','design'),
('restaurant','restaurant')
)

class Blog(models.Model):

    title = models.CharField(max_length=15)
    blog_detail = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blogs/')
    blog_type = models.CharField (max_length=15 , choices = Blog_Type)
    blog_description = models.TextField (max_length=200)
    bloger = models.ForeignKey(Profile,on_delete=models.CASCADE ,default=None)
    published_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,null=True)


    def save (self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog,self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(Profile, verbose_name=("user"), on_delete=models.CASCADE)
    blog= models.ForeignKey(Blog,verbose_name=("blog"),on_delete=models.CASCADE )
    comment= models.TextField(max_length=255)
    published_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user)