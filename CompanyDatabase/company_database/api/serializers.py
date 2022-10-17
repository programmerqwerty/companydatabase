from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Worker, Job, WorkGroup

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class WorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Worker
        fields = ['id', 'name', 'familyName', 'lastName', 'jobs', 'workGroups']

class JobSerializer(serializers.ModelSerializer):
    workers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Job
        fields = ['id', 'name', 'workers']
        
class WorkGroupSerializer(serializers.ModelSerializer):
    workers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    subGroups = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    
    class Meta:
        model = WorkGroup
        fields = ['id', 'name', 'workers', 'parent', 'subGroups']