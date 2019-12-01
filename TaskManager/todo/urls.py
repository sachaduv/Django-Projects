from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name="index"),
    path('addTask',views.addTask,name="addTask"),
    path('complete/<todo_id>',views.complete,name="complete"),
    path('delete_complete',views.delete_complete,name="delete_complete"),
    path('delete_all',views.delete_all,name="delete_all")
]
