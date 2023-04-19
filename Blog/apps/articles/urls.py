from django.urls import path,include
from apps.articles.views import article_list,article_details,article_form,article_update,article_delete
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    path('',article_list, name = 'article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('add-article/', article_form, name='add-article'),
    path('update-article/<slug:slug>/', article_update, name='update-article'),
    path('delete_article/<slug:slug>/', article_delete, name='delete-article'),

    path('social-auth/', include('social_django.urls', namespace='social')),



]
