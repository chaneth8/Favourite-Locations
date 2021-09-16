# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_screen, name='login_screen'),
    path('home/<str:name>/', views.home, name="home"),
    path('add_form/<str:name>/', views.add_form, name='add_form'),
    path('add_form/<str:name>/add', views.add, name='add'),
    path('login', views.login, name='login'),
    path('delete_form/<str:name>/', views.delete_form, name='delete_form'),
    path('delete/<str:name>/', views.delete, name='delete'),
    path('add_comment_form/<str:title>/<str:name>', views.add_comment_form, name='add_comment_form'),
    path('add_comment/<str:title>/<str:name>', views.add_comment, name='add_comment'),
    path('comments/<str:title>/<str:name>', views.comments, name='comments'),
    path('trip_planner/<str:name>/', views.trip_planner, name='trip_planner'),
]

