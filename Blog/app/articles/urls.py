from django.urls import path,include
from app.articles.views import article_list,article_details,user_login,register,article_form,article_update,article_delete
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    path('',article_list, name = 'article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    # path('login/', user_login, name='user_login'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', register, name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('add-article/', article_form, name='add-article'),
    path('update-article/<slug:slug>/', article_update, name='update-article'),
    path('delete_article/<slug:slug>/', article_delete, name='delete-article'),

    path('social-auth/', include('social_django.urls', namespace='social')),



]
