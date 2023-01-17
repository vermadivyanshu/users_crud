from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import AppUser
from django.urls import reverse_lazy
from .forms.app_user_form import AppUserForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

class UserListView(ListView):
    template_name = 'users.html'
    model = AppUser
    ordering = '-created_at'
    context_object_name = 'users'
    extra_context = {'heading': 'Team members'}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users_length = len(context['users'])
        if users_length == 1:
            context['sub_heading'] = 'You have 1 team member'
        else:
            context ['sub_heading'] = 'You have ' + str(users_length) + ' team members'
        return context

class CreateUserView(CreateView):
    template_name = 'create_user_view.html'
    form_class = AppUserForm
    extra_context = {'heading': 'Add a team member', 'sub_heading': 'Set email, location and role', 'action': 'POST'}
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'id'
    http_method_names = ['get', 'post']

class EditUserView(UpdateView):
    template_name='edit_user_view.html'
    extra_context = {'heading': 'Edit a team member', 'sub_heading': 'Edit email, location and role', 'action': 'POST'}
    success_url = reverse_lazy('index')
    form_class = AppUserForm
    model = AppUser
    pk_url_kwarg='id'
    http_method_names = ['get', 'post']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs['id']
        return context

class DeleteUserView(DeleteView):
    pk_url_kwarg = 'id'
    http_method_names=['post']
    model= AppUser
    pk_url_kwarg ='id'
    success_url = '/users/'
    http_method_names = ['post']
