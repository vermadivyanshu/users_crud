from django.db import models
from django.core.validators import RegexValidator

# AppUsers model
class AppUser(models.Model):
  email = models.EmailField(unique=True, blank=False, null=False)
  first_name = models.CharField(max_length=250, null=False, blank=False)
  last_name = models.CharField(max_length=250, null=True, blank=True)
  phone_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$', message='Invalid phone')])
  # this could be turned into an enum for better readbility or extended to
  # it's own master table if needed, but using a boolean flag for simplicity.
  is_admin = models.BooleanField(default=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(auto_now=True)

  @classmethod
  def get_all_ordered_by_created_at(self):
    return self.objects.all().order_by('-created_at')
  
  @property
  def full_name(self):
    return self.first_name + ' ' + self.last_name;

