from django.urls import path, re_path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path(r'^post/(?P<pk>[1-9][0-9]*)/$', views.PostDetailView.as_view(),
            name='post')
]
