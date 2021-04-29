from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import DetailView


def post_list(request):
    posts = Post.objects.order_by('-publish')
    return render(request, 'blog/post/list.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post_detail'
