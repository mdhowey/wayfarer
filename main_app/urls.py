from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name="profile_update"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('cities/', views.CityList.as_view(), name="city_list"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('post/<int:pk>/', views.PostList.as_view(), name = 'post_show'),
    path('post/create/', views.PostCreate.as_view(), name = 'post_create')
]
