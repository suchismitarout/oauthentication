from django.urls import path
from . import views
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout, name='logout'),
    path('delete/<post_id>/', views.delete_post, name='delete_post'),
]


