from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
     path('posts/', views.show_posts, name='show_posts'),
     path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
     path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]
