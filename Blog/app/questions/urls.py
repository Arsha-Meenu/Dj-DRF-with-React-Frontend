from django.urls import path
from .views import *

urlpatterns = [
    path('list/', question_list,name = 'question-list'),
]