from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('<str:username>/', views.specificUserBlogs, name="specific-user-blogs"),
    path('<str:pk>/detail/', views.detailBlog, name="blog-detail"),
    path('create/', views.createBlog, name="blog-create"),
    path('<str:pk>/update/', views.updateBlog, name="blog-update"),
    path('<str:pk>/delete/', views.deleteBlog, name="blog-delete"),
    path('about/', views.about, name="blog-about"),
]
