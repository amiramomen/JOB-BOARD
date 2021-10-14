from django.shortcuts import render
from job.models import Job
from accounts.models import Profile
# Create your views here.


def home (request):
 job_list = Job.objects.all()
 profiles = Profile.objects.all()
 print(profiles,job_list)
 return render(request,'home/index.html' , {'jobs':job_list,'profiles':profiles} )