from rest_framework import serializers 
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    members=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True
    )
    class Meta:
        model=Project
        fields= ['name','description', 'status','created_by', 'members','created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields= '__all__'