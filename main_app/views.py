from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Profile extension commented out
# from .models import Profile

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class Profile(TemplateView):
    template_name = 'profile.html'

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)






# PROFILE EXTENSION WORK COMMENTED OUT BELOW

# Create your views here.
# class Signup(View):

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("base")
#         else:
#             context = {"form": form}
#             return render(request, "home.html", context)


# class Signup(View):
#     # @login_required
#     # @transaction.atomic
#     def update_profile(request):
#         if request.method == 'POST':
#             user_form = UserForm(request.POST, instance=request.user)
#             profile_form = ProfileForm(request.POST, instance=request.user.profile)
#             if user_form.is_valid() and profile_form.is_valid():
#                 user_form.save()
#                 profile_form.save()
#                 messages.success(request, _('Your profile was successfully updated!'))
#                 return redirect('settings:profile')
#             else:
#                 messages.error(request, _('Please correct the error below.'))
#         else:
#             user_form = UserForm(instance=request.user)
#             profile_form = ProfileForm(instance=request.user.profile)
#         return render(request, 'profiles/profile.html', {
#             'user_form': user_form,
#             'profile_form': profile_form
#         })

# class home(View):

#     def get(self, request):
#         return render(request, 'home.html')

#     def update_profile(request):
#         if request.method == 'POST':
#             user_form = UserForm(request.POST, instance=request.user)
#             profile_form = ProfileForm(request.POST, instance=request.user.profile)
#             if user_form.is_valid() and profile_form.is_valid():
#                 user_form.save()
#                 profile_form.save()
#                 messages.success(request, _('Your profile was successfully updated!'))
#                 return redirect('settings:profile')
#             else:
#                 messages.error(request, _('Please correct the error below.'))
#         else:
#             user_form = UserForm(instance=request.user)
#             profile_form = ProfileForm(instance=request.user.profile)
#         return render(request, 'profiles/profile.html', {
#             'user_form': user_form,
#             'profile_form': profile_form
#         })
