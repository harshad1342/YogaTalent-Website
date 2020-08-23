from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
    # # API to post comment
    # path('postComment', views.postComment, name="postComment"),

    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]
