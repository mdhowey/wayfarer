from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/edit/', views.ProfileUpdate.as_view(), name="profile_update"),
    path('profile/<int:pk>/create/', views.ProfileCreate.as_view(), name="profile_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('post/create/', views.PostCreate.as_view(), name = 'post_create'),
    path('post/<int:pk>/', views.PostShow.as_view(), name = 'post_show'),
    path('post/<int:pk>/edit', views.PostUpdate.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name = 'post_delete'),
]