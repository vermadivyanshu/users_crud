from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import AppUser
from django.urls import reverse
from django.views import View
from .forms.app_user_form import AppUserForm
from django.http import Http404, HttpResponseServerError
from django.db import connection

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
            # form.save()
            data = form.cleaned_data
            try:
                cursor = connection.cursor()
                cursor.execute('''INSERT INTO userlist_appuser (email, first_name, last_name, phone_number, is_admin, created_at, updated_at) VALUES(%s, %s, %s, %s, %s, NOW(), NOW())''', [
                    data['email'], data['first_name'], data['last_name'], data['phone_number'],
                    data['is_admin']
                ])
                # form.save();
                cursor.close()
                return redirect(reverse('index'))
            except Exception:
                # return 500
                raise HttpResponseServerError
        return render(request, self.template_name, {'form': form, **self.context})


class EditUserView(View):
    template_name='edit_user_view.html'
    context = {'heading': 'Edit a team member', 'sub_heading': 'Edit email, location and role', 'action': 'POST'}
    form_class = AppUserForm
    def get(self, request, id):
        # app_user = get_object_or_404(AppUser, id=id)
        app_user = AppUser.objects.raw('SELECT * from userlist_appuser where id = %s', [id])[0]
        if (app_user):
          form = self.form_class(instance=app_user)
          context = {'form': form, 'user_id': id, **self.context }
          return render(request, self.template_name, context)
        else:
            raise Http404
    
    def post(self, request, id):
        # app_user = get_object_or_404(AppUser, id=id)
        app_user = AppUser.objects.raw('SELECT * from userlist_appuser WHERE id = %s', [id])[0]
        if(app_user):
            form = self.form_class(request.POST, instance=app_user)
            if form.is_valid():
                data = form.cleaned_data
                try:
                    cursor = connection.cursor()
                    cursor.execute(''' UPDATE userlist_appuser SET (email, first_name, last_name, phone_number, is_admin, updated_at)
                    = (%s, %s, %s, %s, %s, NOW()) WHERE id = %s''', [
                        data['email'], data['first_name'], data['last_name'], data['phone_number'],
                        data['is_admin'], id
                    ]) 
                    # form.save();
                    cursor.close()
                    return redirect(reverse('index'))
                except Exception:
                    # return 500
                    raise HttpResponseServerError 
            context = {'form': form, 'user_id': id, **self.context}
            return render(request, self.template_name, context)
        else:
            raise Http404

class DeleteUserView(View):
    def post(self, request, id):
        app_user = AppUser.objects.raw('SELECT * FROM userlist_appuser WHERE id = %s', [id])[0]
        # app_user = get_object_or_404(AppUser, id=id)
        if(app_user):
            try:
                cursor = connection.cursor()
                cursor.execute(
                    'DELETE FROM userlist_appuser WHERE id = %s', [id]
                )
                cursor.close()
                return redirect(reverse('index'))
            except Exception:
                raise HttpResponseServerError
        else:
            raise Http404
