# view
from .models import Job
from .Serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



@api_view(['GET'])
def jobs_api (request):
    jobs = Job.objects.all()
    data = JobSerializer(jobs,many = True).data
    return Response({'data':data})

    
@api_view(['GET'])
def job_api_detail (request,id):
    job = Job.objects.get(id=id)
    data = JobSerializer(job).data
    return Response({'data':data})

    
class JobsList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'