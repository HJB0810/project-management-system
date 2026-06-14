from .views import dashboard_view
from django.urls import path,include


urlpatterns = [
    path('',dashboard_view,name='dashboard')
]