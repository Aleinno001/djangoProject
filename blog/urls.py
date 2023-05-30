from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('manage-post/', views.managePost, name='managePost'),
    path('manage-post/create-post/', views.createPost, name='createPost'),
    path('manage-post/save-post/', views.savePost, name='savePost'),
    path('manage-post/delete/<slug:postid>', views.delete, name='delete'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
]
