from django.urls import path
from .views import *

urlpatterns = [
    path('', question_list,name ='question-list'),
    path('create/', question_create, name='question-create'),
    path('details/<slug:slug>/', question_details, name='question-details'),
    path('update/question/<slug:slug>/', question_update, name='question-update'),
    path('delete/question/<slug:slug>/', question_delete, name='question-delete'),
    path('update/answer/<int:id>/', answer_update, name='answer-update'),
    path('delete/answer/<int:id>/', answer_delete, name='answer-delete'),
    path('list/', list_question_answer, name='list-question-answer'),

]
