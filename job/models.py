from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
Job_Type = (
('part time','part time'),
('full time','full time')
)

def get_image_name(instance, filename):
        fn = 'jobs/%s.jpg' % instance.id
        return fn

class Job (models.Model):
    title = models.CharField(max_length=100) 
    job_type = models.CharField(max_length=15,choices= Job_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image= models.ImageField(upload_to=get_image_name)
    slug = models.SlugField(blank=True,null=True)

    def save (self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)



    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name 