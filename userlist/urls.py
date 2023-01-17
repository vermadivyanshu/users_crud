from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserListView, CreateUserView, EditUserView, DeleteUserView

urlpatterns = [
    path('', login_required(UserListView.as_view()), name='index'),
    path('add/', login_required(CreateUserView.as_view()), name='create'),
    path ('<int:id>/', login_required(EditUserView.as_view()), name='edit'),
    path('delete/<int:id>/', login_required(DeleteUserView.as_view()), name='delete')
]