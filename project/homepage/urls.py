from django.urls import path, re_path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('create_tag/', views.CreateTagView.as_view(), name='create_tag'),
    re_path(r'^post/(?P<pk>[1-9][0-9]*)/$', views.PostDetailView.as_view(),
            name='post'),
    re_path(r'^like/(?P<pk>[1-9][0-9]*)/$', views.likeView,
            name='like')
]
