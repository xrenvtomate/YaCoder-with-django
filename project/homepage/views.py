from django.views.generic.list import ListView

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'homepage/homepage.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.published_main()
