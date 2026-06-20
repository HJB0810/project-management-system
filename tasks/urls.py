from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_list,name='task_list'),
    path('create/',views.task_create,name='task_create'),
    path('<int:pk>/edit/',views.task_update,name='task_update'),
    path('<int:pk>/delete/',views.task_delete,name='task_delete'),
    path('get-members/<int:project_id>/',views.get_project_members,name='get_project_members')
]