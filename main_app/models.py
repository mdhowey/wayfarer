# from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser,  
# from django.utils.translation import ugettext_lazy as _

# # Create your models here.
# class User(AbstractBaseUser):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     profile_img = models.ImageField(upload_to='profile/', null=True, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [
#         'email',
#         'first_name',
#         'last_name',
#     ]

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

# from django.contrib.auth.models import User

# class Person(User):
#     def __init__(self):
#         super().__init__()

#     class Meta:
#         proxy = True
#         current_city = ('current_city')