from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/view/<pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<pk>/', views.post_edit, name='post_edit'),
    path('post/erase/<pk>/', views.post_erase, name='post_erase'),
]