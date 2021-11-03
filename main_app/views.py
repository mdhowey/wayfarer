from django.contrib.auth import models
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from .models import Comment, Post, City, Profile
from django.contrib.auth.models import User

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self):
        user = self.request.user
        user_profile = Profile.objects.get(user_id=self.request.user.id)
        context = {}
        context["posts"] = Post.objects.filter(user=user)
        context["header"] = f"{user}'s posts"
        context["profile"] = user_profile
        return context


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['name', 'current_city', 'img', 'bio']
    template_name = "profile_create.html"
    success_url = "/profile/"
 
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["user"] = User.objects.get(id=self.request.user.id)
        return context

    def post(self, request, pk):
        user_id = request.POST.get("user_id")
        user = request.POST.get("user")
        name = request.POST.get("name")
        current_city = request.POST.get("current_city")
        img = request.POST.get("img")
        bio = request.POST.get("bio")
        Profile.objects.create(user_id=user_id, user=user, name=name, current_city=current_city, img=img, bio=bio)
        return redirect('profile')


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['name', 'current_city', 'img', 'bio']
    template_name = "profile_update.html"
    success_url = "/profile/"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class CityList(TemplateView):
    template_name = 'city_list.html'

    def get_context_data(self):
        context = {}
        context["cities"] = City.objects.all()
        context["header"] = f"All city posts"
        return context

class CityDetail(TemplateView):
    template_name = "city_detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super(CityDetail, self).get_context_data(**kwargs)
        context["city"] = City.objects.filter(id=pk)
        context["posts"] = Post.objects.filter(city=pk)
        return context

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
            return redirect('profile_create', pk=self.request.user.id)
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'img', 'body']
    template_name = "post_create.html"

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context["city"] = City.objects.all()
        context["user"] = User.objects.get(id=self.request.user.id)
        return context

    def post(self, request):
        user_id = request.POST.get("user_id")
        title = request.POST.get("title")
        img = request.POST.get("img")
        body = request.POST.get("body")
        city = City.objects.get(name=request.POST.get("city"))
        Post.objects.create(user_id=user_id, title=title, img=img, city=city, body=body)
        return redirect('city_list')

class PostShow(DetailView):
    model = Post
    template_name = "post_show.html"

class CommentList(DetailView):
    model = Comment
    template_name = "comment_list.html"

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'img', 'body', 'city']
    template_name = "post_update.html"
    success_url = "/cities/"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/cities/"

    def test_func(self):
        obj = self.get_object();
        return obj.user == self.request.user
        





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
