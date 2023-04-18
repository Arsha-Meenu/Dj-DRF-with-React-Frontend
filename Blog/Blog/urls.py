from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('articles/',include('app.articles.urls')),
    path('questions/',include('app.questions.urls')),
    path('admin/', admin.site.urls),
]
