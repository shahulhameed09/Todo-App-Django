from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.logins, name="logins"),
    path('logout', views.logouts, name="logout"),
    path('register', views.reg, name="register"),

    path('task', views.task, name="task"),
    path('task_edit/<request_ID>', views.task_edit, name="task_edit"),
    path('delete_task/<request_ID>', views.delete_task, name="delete_task"),
    path('add_task', views.add_task, name="add_task"),
]