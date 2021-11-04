from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length = 100)
    current_city = models.CharField(max_length = 100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    population = models.IntegerField(default=0)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.body

# Profile extension commented out (Howey and Michael approach below)

# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import User

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


# class Person(User):
#     def __init__(self):
#         super().__init__()

#     class Meta:
#         proxy = True
#         current_city = ('current_city')




# Profile extension commented out (Phil and Apoorva approach below)

# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
