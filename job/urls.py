
from django.urls import path , include
from .import views
from . import api
app_name = 'job'

urlpatterns = [
    path('',views.job_list,name='job_list' ),
    path('add',views.add_job,name='add_job'), 
    path('<str:slug>',views.job_detail, name='job_detail'),  
    

    #api 
    path('api/jobs',api.jobs_api,name='jobs_api'), 
    path('api/jobs/<int:id>',api.job_api_detail, name='job_api_detail'),  

   # api class based views 

   path('api/v2/jobs',api.JobsList.as_view(),name='jobs_list'), 
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view(), name='job_detail'), 
]
