from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Worker, Job, WorkGroup


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class WorkerList(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = serializers.WorkerSerializer

class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = serializers.WorkerSerializer
    
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer

class WorkGroupList(generics.ListCreateAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = serializers.WorkGroupSerializer

class WorkGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkGroup.objects.all()
    serializer_class = serializers.WorkGroupSerializer