from django.urls import path 
from .views import edit_tasks, list_tasks, create_tasks, delete_tasks, update_tasks

urlpatterns = [
    path('',list_tasks),
    path('new/',create_tasks, name='create_tasks'),
    path('delete_task/<int:task_id>/', delete_tasks, name='delete_tasks'),
    path('update_task/<int:task_id>/', update_tasks, name='update_tasks'),
    path('edit_task/', edit_tasks, name='edit_tasks')
]