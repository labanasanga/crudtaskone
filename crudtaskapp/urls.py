from django.urls import path
from . import views

urlpatterns = [
   path('', views.task_list, name='task_list'),
    path('detail/<int:id>/', views.task_detail, name='task_details '),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:id>/', views.task_update, name=''),
    path('delete/<int:id>/', views.task_delete, name='')
]