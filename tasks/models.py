from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES=[
        ('To Do','To Do'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    ]
    PRIORITY_CHOICE=[
        ('low','low'),
        ('medium','medium'),
        ('high','high')
    ]
    title=models.CharField( max_length=200)
    description=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='tasks')
    assigned_to =models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=25,choices=STATUS_CHOICES,default='To Do')
    priority=models.CharField(max_length=25,choices=PRIORITY_CHOICE,default='Medium')
    due_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title