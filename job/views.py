from job.form import Applyform
from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from .form import Applyform , Addjob
from django.urls import reverse


# Create your views here.
def job_list (request):
 list = Job.objects.all()
 paginator = Paginator(list, 2)
 page_number = request.GET.get('page')
 page_obj = paginator.get_page(page_number)
 njob = Job.objects.all().count() 
 context={'jobs': page_obj,'Njob':njob} 
 return render(request,'job/job_list.html',context)



def job_detail(request,slug):
  detail=Job.objects.get(slug=slug)

  if request.method == 'POST':
    form = Applyform (request.POST, request.FILES)
    if form.is_valid(): 
      myform=form.save(commit=False)
      myform.job=detail
      myform.save()
  
  else:
    form = Applyform()
    context = {'job':detail,'formm':form}
  return render(request,'job/job_detail.html',context)



def add_job(request):
    if request.method == 'POST':
      form = Addjob(request.POST , request.FILES)
      if form.is_valid():
         myform=form.save(commit=False)
         myform.owner=request.user
         myform.save()
         return redirect (reverse('jobs:job_list'))

    else:
      form=Addjob()
    return render(request,'job/job_post.html',{'form':form})
