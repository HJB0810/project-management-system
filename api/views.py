from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from projects.models import Project
from tasks.models import Task
from .serializers import ProjectSerializer,TaskSerializer
from django.db.models import Q

class ProjectViewSet(viewsets.ModelViewSet):
    queryset =Project.objects.all()
    serializer_class=ProjectSerializer
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(
            Q(created_by=self.request.user)|
            Q(members=self.request.user)
        ).distinct()
    def perform_create (self,serializer):
        serializer.save(
            created_by=self.request.user
        )

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    permission_classes =[IsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(
            assigned_to=self.request.user
        )
    def perform_create (self,serializer):
        serializer.save()