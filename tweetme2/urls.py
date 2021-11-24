"""tweetme2 URL Configuration"""
from django.contrib import admin
from django.urls import path, re_path  # url()
from tweets.views import home_view
from tweets.views import tweet_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('tweets/<int:tweet_id>', tweet_detail_view)
]
