from django.conf.urls import url
from . import views
from .models import Post
from django.urls import path

urlpatterns = [
    # post views
    url('', views.post_list, name='post_list'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]