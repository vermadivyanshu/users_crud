from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import AppUser
from django.urls import reverse
from django.views import View
from .forms.app_user_form import AppUserForm

# Create your views here.

class UserListView(View):
    template_name = 'users.html'
    def get(self, request):
        users = AppUser.get_all_ordered_by_created_at()
        context = {'users': users, 'heading': 'Team members'}
        if len(users) == 1:
            context['sub_heading'] = 'You have 1 team member'
        else:
            context ['sub_heading'] = 'You have ' + str(len(users)) + ' team members'
        return render(request, self.template_name, context)

class CreateUserView(View):
    template_name = 'create_user_view.html'
    form_class = AppUserForm
    context = {'heading': 'Add a team member', 'sub_heading': 'Set email, location and role', 'action': 'POST'}
    def get(self, request):
        context = { 'form': self.form_class(), **self.context}
        return render(request, self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        return render(request, self.template_name, {'form': form, **self.context})


class EditUserView(View):
    template_name='edit_user_view.html'
    context = {'heading': 'Edit a team member', 'sub_heading': 'Edit email, location and role', 'action': 'POST'}
    form_class = AppUserForm
    def get(self, request, id):
        app_user = get_object_or_404(AppUser, id=id)
        form = self.form_class(instance=app_user)
        context = {'form': form, 'user_id': id, **self.context }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        app_user = get_object_or_404(AppUser, id=id)
        form = self.form_class(request.POST, instance=app_user)
        if form.is_valid():
            form.save();
            return redirect(reverse('index'))
        context = {'form': form, 'user_id': id, **self.context}
        return render(request, self.template_name, context)

class DeleteUserView(View):
    def post(self, request, id):
        app_user = get_object_or_404(AppUser, id=id)
        app_user.delete();
        return redirect(reverse('index'))
