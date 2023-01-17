from django.test import TestCase
from .models import AppUser
from django.contrib.auth import get_user_model

User = get_user_model()

class TestUserListView(TestCase):

  def setUp(self):
    self.user = User.objects.create(username='test')
    self.user.set_password('test')
    self.user.save()
    self.client.login(username='test', password='test')
  
  def test_user_list_view(self):
    AppUser.objects.create(email='a@test.com', first_name='test1', last_name='test2', phone_number='343-558-7788')
    response = self.client.get('/users/')
    self.assertEqual(response.status_code, 200)
  
  def test_get_valid_user(self):
    user = AppUser.objects.create(email='a@test.com', first_name='test1', last_name='test2', phone_number='343-558-7788')
    response = self.client.get('/users/' + str(user.id)+ '/')
    self.assertEqual(response.status_code, 200)
  
  def test_get_invalid_user(self):
    response = self.client.get('/users/123/')
    self.assertEqual(response.status_code, 404)
  
  def test_edit_invalid_user(self):
    response = self.client.post('/users/123/')
    self.assertEqual(response.status_code, 404)
  
  def test_create_valid_user(self):
    payload = {
      'email': 'a@test.com',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '343-558-8877',
      'is_admin': True
    }
    self.assertEqual(len(AppUser.get_all_ordered_by_created_at()), 0)
    response = self.client.post('/users/add/',payload)
    self.assertRedirects(response, expected_url='/users/')
    users = AppUser.get_all_ordered_by_created_at()
    self.assertEqual(len(users), 1)
  
  def test_create_invalid_input(self):
    payload = {
      'email': 'a@test.com',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '34-558-8877',
      'is_admin': True
    }
    self.assertEqual(len(AppUser.get_all_ordered_by_created_at()), 0)
    response = self.client.post('/users/add/',payload)
    self.assertEqual(len(AppUser.get_all_ordered_by_created_at()), 0)
    self.assertEqual(response.status_code, 200)
  
  def test_edit_valid_user(self):
    user = AppUser.objects.create(email='a@test.com', first_name='test1', last_name='test2', phone_number='343-558-7788')
    payload = {
      'email': 'a@test.com',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '343-558-8877',
      'is_admin': True
    }
    response = self.client.post('/users/' + str(user.id)+ '/',payload)
    self.assertRedirects(response, expected_url='/users/')
    user.refresh_from_db()
    self.assertEqual(user.is_admin, True)
  
  def test_edit_invalid_input(self):
    user = AppUser.objects.create(email='a@test.com', first_name='test1', last_name='test2', phone_number='343-558-7788')
    payload = {
      'email': 'a@test.com',
      'first_name': 'test1',
      'last_name': 'test2',
      'phone_number': '34-558-8877',
      'is_admin': True
    }
    response = self.client.post('/users/' + str(user.id)+ '/',payload)
    self.assertEqual(response.status_code, 200)
    user.refresh_from_db()
    # attributes remain unchanged in the database
    self.assertEqual(user.phone_number, '343-558-7788')
    self.assertEqual(user.is_admin, False)
  
  def test_delete_valid_user(self):
    user = AppUser.objects.create(email='a1@test.com', first_name='test1', last_name='test2', phone_number='343-558-7788')
    response = self.client.post('/users/delete/'+ str(user.id) + '/')
    self.assertRedirects(response, expected_url='/users/')
  
  def test_delete_invalid_user(self):
    response = self.client.post('/users/delete/123/')
    self.assertEqual(response.status_code, 404)
    