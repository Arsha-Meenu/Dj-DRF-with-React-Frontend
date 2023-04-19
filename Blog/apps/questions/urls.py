from django.urls import path
from .views import *

urlpatterns = [
    path('', question_list,name ='question-list'),
    path('create/', question_create, name='question-create'),
    path('details/<slug:slug>/', question_details, name='question-details'),
    path('update/<slug:slug>/', question_update, name='question-update'),
    path('delete/<slug:slug>/', question_delete, name='question-delete'),

]
