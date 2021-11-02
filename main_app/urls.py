from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('profile/edit/<int:pk>', views.ProfileEdit.as_view(), name="profile_edit"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('post/<int:pk>/', views.PostList.as_view(), name = 'post_show'),
]
