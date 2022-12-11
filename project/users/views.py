from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import ProfileForm, SignUpForm
from .models import User


class SignUpView(CreateView):
    template_name = 'users/signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage:home')

    def form_invalid(self, form):
        return render(self.request, 'users/signup.html',
                      {'form': form})

    def get_form(self):
        return SignUpForm(self.request.POST or None)


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    pk = 1
    model = User
    form_class = ProfileForm

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('homepage:home')

    def get_form(self):
        return ProfileForm(self.request.POST or None,
                           instance=self.request.user)


class UsersView(ListView):

    template_name = 'users/user_list.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = User
    context_object_name = 'disp_user'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])
