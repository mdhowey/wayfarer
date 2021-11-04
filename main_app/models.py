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

    class Meta:
        ordering = ['name']

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