from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'homepage/homepage.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.published_main()


class PostDetailView(DetailView):
    model = Post
    template_name = 'homepage/post.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])
