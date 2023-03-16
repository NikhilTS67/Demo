from django.urls import path
from . import views
app_name = 'Todo_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:ID>/', views.delete, name='delete'),
    path('update/<int:ID>/', views.update, name='update'),
    path('cbvhome/', views.TaskListview.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailsview.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),
]