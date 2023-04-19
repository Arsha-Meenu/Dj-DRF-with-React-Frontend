from django.shortcuts import render,get_object_or_404,redirect
from .models import Question,Answer
from .forms import QuestionCreateForm,AnswerCreateForm

def question_list(request):
    question_list = Question.objects.all().order_by('-created_at')
    return render(request,'questions/question_list.html',{'question_list':question_list})


def question_details(request,slug):
    question = get_object_or_404(Question,slug = slug)
    answers = Answer.objects.filter(question = question)
    # adding answer
    if request.method == 'POST':

        form = AnswerCreateForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question-details',slug = question.slug)
    else:
        form = AnswerCreateForm()
    return  render(request,'questions/question_details.html',{'question':question,'answers':answers,'form':form})

def question_create(request):
    if request.method == 'POST':
        question_form = QuestionCreateForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question-list')
    else:
        question_form = QuestionCreateForm()
    return render(request,'questions/create_question.html',{'question_form':question_form})

def question_update(request,slug):
    question = get_object_or_404(Question,slug = slug)
    question_form = QuestionCreateForm(request.POST or None,instance=question)
    if question_form.is_valid():
        question_form.save()
        return redirect('question-list')
    return render(request, 'questions/create_question.html', {'question_form': question_form})


def question_delete(request,slug):
    question = get_object_or_404(Question,slug = slug)
    question.delete()
    return redirect('question-list')