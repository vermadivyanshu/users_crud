from django.test import TestCase
from .models import AppUser
from .forms.app_user_form import AppUserForm


# Create your tests here.

class TestAppUser(TestCase):
  def test_no_users(self):
    self.assertEquals(len(AppUser.get_all_ordered_by_created_at()),0)
  
  def test_users_ordered_by_created_at(self):
    user_1 = AppUser.objects.create(email='a@test.com', first_name='test1', last_name='test2', phone_number='343-558-7788')
    user_2 = AppUser.objects.create(email='b@test.com', first_name='test3', last_name='test2', phone_number='347-558-7788')
    results = AppUser.get_all_ordered_by_created_at()
    self.assertEqual(len(results), 2)
    self.assertEqual(results[0].email, user_2.email)
    self.assertEqual(results[1].email, user_1.email)

