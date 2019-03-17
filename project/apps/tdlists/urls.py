from django.urls import path

from . import views

urlpatterns = [
    path('', views.lists, name='tdlists'),
    path('add_task', views.add_task, name='add_task'),
    path('check/<int:task_id>', views.check, name='check'),
    path('delete/<int:task_id>', views.delete, name='delete_task'),
    path('edit/<int:task_id>', views.edit, name='edit_task'),

]