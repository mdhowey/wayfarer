from django.contrib import admin
from .models import City, Post, Profile

# Profile extension commented out
# from .models import Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(City)
admin.site.register(Profile)

# Profile extension commented out
# admin.site.register(Profile)
