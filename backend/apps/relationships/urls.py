from django.urls import path
from . import views

app_name = 'relationships'

urlpatterns = [
    path('follow/<int:pk>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:pk>/', views.unfollow_user, name='unfollow_user'),
]
