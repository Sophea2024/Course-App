from django.urls import path
from . import views

urlpatterns = [
    path('', views.mitglieder, name='mitglieder'),
    path('members/', views.allMembers, name='members'),
    path('members/details/<int:id>', views.details, name='details')
]