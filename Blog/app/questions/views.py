from django.shortcuts import render
from .models import Question


def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request,'questions/question_list.html',{'question_list':question_list})
