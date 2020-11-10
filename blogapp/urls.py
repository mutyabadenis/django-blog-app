from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'blogapp'

urlpatterns = [
    url(r'^create/$',views.article_create, name='create'),
    path('articles',views.blog_list, name='articlelist'),
    path('home', views.blog_list, name='home'),
    path('about', views.about),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name='details'),
]