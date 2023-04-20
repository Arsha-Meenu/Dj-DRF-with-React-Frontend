from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('articles/',include('apps.articles.urls')),
    path('questions/',include('apps.questions.urls')),
    path('', include('apps.users.urls')),
    path('admin/', admin.site.urls),
]
