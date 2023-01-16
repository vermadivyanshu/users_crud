from django import forms
from django.core.validators import RegexValidator
from ..models import AppUser

ROLES = [
        (True, "Regular - Can't delete members"),
        (False, 'Admin - Can delete members'),
    ]

class AppUserForm(forms.ModelForm):
  first_name = forms.CharField(label='First Name',required=True, max_length=250,
    error_messages={'required': 'First Name is required', 'max_length': 'First Name has upto 250 characters'},
    widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'First Name'}))
  last_name = forms.CharField(label='Last Name', required=False, max_length=250,
  error_messages={'max_length': 'Last Name has upto 250 characters'},
  widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'Last Name'}))
  email = forms.EmailField(label='Email',required=True,
  error_messages={'required': 'Email is required'},
  widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'Email'}))
  phone_number = forms.CharField(label='Phone Number', max_length=12,
  error_messages={'max_length': 'Phone Number has 12 characters'},
  validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$', message='Invalid phone number format ')],
  widget=forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'Phone Number'}))
  is_admin = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=ROLES,
        initial=True 
    )
  template_name = 'app_user_form.html'
  class Meta:
    model = AppUser
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'is_admin']