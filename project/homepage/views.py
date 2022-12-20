from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.list import ListView

from .forms import CommentForm, PostForm
from .models import Comment, Post


class HomeView(ListView):
    paginate_by = 9
    model = Post
    template_name = 'homepage/homepage.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.published_main().order_by('popularity')


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'homepage/post.html'
    context_object_name = 'post'
    form_class = CommentForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            comment_text = form.cleaned_data['text']
            user = self.request.user
            post = self.get_object()
            Comment.objects.create(
                text=comment_text,
                user=user,
                post=post,
            )
            return redirect('homepage:post', pk=self.kwargs['pk'])
        else:
            return self.form_invalid(form)

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.select_by_new().filter(
            post=self.kwargs['pk'],
        )
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'homepage/create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.save()
        return redirect('homepage:home')

    def form_invalid(self, form):
        return render(self.request, 'homepage/create_post.html',
                      {'form': form})
