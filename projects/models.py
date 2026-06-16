from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    STATUS_CHOICES =(
        ('Pending','Pending'),
        ('In-process','In-process'),
        ('Completed','Completed')
    )

    name=models.CharField(max_length=200)
    description=models.TextField()
    created_by =models.ForeignKey(
          User,
          on_delete=models.CASCADE
          )
    status=models.CharField(
          max_length=20,
          choices=STATUS_CHOICES,
          default='Pending'
          )
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
