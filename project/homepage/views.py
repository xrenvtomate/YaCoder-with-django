from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import PostForm
from .models import Post


class HomeView(ListView):
    paginate_by = 9
    model = Post
    template_name = 'homepage/homepage.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.published_main().order_by('popularity')


class PostDetailView(DetailView):
    model = Post
    template_name = 'homepage/post.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'homepage/create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        print('/////')
        form.save()
        print('//////////////////')
        return redirect('homepage:home')

    def form_invalid(self, form):
        return render(self.request, 'homepage/create_post.html',
                      {'form': form})
