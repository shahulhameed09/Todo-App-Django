from django.urls import path, include
from django.contrib.auth import views as auth_views
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
    
    
        # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]