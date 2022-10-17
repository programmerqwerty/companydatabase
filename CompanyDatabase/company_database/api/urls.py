from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('workers/', views.WorkerList.as_view()),
    path('workers/<int:pk>/', views.WorkerDetail.as_view()),
    path('jobs/', views.JobList.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('workgroups/', views.WorkGroupList.as_view()),
    path('workgroups/<int:pk>/', views.WorkGroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)