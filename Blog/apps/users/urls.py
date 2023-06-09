from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from .views import register,profile_change,profile_redirect



urlpatterns = [
    # path('login/', user_login, name='user_login'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', register, name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    # path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile-change/', profile_change, name='profile-change'),
    path('redirect/', profile_redirect, name='profile-redirect'),

]
