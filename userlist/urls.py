from django.urls import path
from .views import UserListView, CreateUserView, EditUserView, DeleteUserView

urlpatterns = [
    path('', UserListView.as_view(), name='index'),
    path('add/', CreateUserView.as_view(), name='create'),
    path ('<int:id>/', EditUserView.as_view(), name='edit'),
    path('delete/<int:id>/', DeleteUserView.as_view(), name='delete')
]