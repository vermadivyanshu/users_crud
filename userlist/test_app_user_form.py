from django.test import TestCase
from .forms.app_user_form import AppUserForm

class TestAppUserForm(TestCase):
  def test_valid_user_form(self):
    form = AppUserForm({
      'email': 'a@test.com',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '343-558-8877',
      'is_admin': True
    })
    self.assertTrue(form.is_valid())
  
  def test_invalid_email(self):
    form = AppUserForm({
      'email': 'hi',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '343-558-8877',
      'is_admin': True
    })
    self.assertFalse(form.is_valid())
  
  def test_invalid_phone(self):
    form = AppUserForm({
      'email': 'hi@test.com',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '34-558-8877',
      'is_admin': True
    })
    self.assertFalse(form.is_valid())
  
  def test_user_without_last_name(self):
    form = AppUserForm({
      'email': 'user2@test.com',
      'first_name': 'test1',
      'phone_number': '343-558-8877',
      'is_admin': True
    })
    self.assertTrue(form.is_valid())
  
  def test_user_without_first_name(self):
    form = AppUserForm({
      'email': 'user@test.com',
      'last_name':'last',
      'phone_number': '343-558-8877',
      'is_admin': False
    })
    self.assertFalse(form.is_valid())
  
  def test_user_empty_email(self):
    form = AppUserForm({
      'email': '',
      'first_name': 'first',
      'last_name': 'last',
      'phone_number': '343-558-8877',
      'is_admin': False
    })
    self.assertFalse(form.is_valid())
  
