from django.shortcuts import render,get_object_or_404,redirect
from .models import Question,Answer
from .forms import QuestionCreateForm,AnswerCreateForm
from django.contrib.auth.decorators import login_required


@login_required
def question_list(request):

    if 'search' in request.GET:
        search = request.GET['search']
        question_list = Question.objects.filter(title__icontains = search).order_by('-created_at')
    else:
        question_list = Question.objects.all().order_by('-created_at')
    return render(request,'questions/question_list.html',{'question_list':question_list})

@login_required
def question_details(request,slug):
    question = get_object_or_404(Question,slug = slug)
    answers = Answer.objects.filter(question = question)
    # adding answer
    if request.method == 'POST':
        answer_form = AnswerCreateForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question-details',slug = question.slug)
    else:
        answer_form = AnswerCreateForm()
    return  render(request,'questions/question_details.html',{'question':question,'answers':answers,'answer_form':answer_form})


@login_required
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


@login_required
def question_update(request,slug):
    question = get_object_or_404(Question,slug = slug)
    question_form = QuestionCreateForm(request.POST or None,instance=question)
    if question_form.is_valid():
        question_form.save()
        return redirect('question-list')
    return render(request, 'questions/create_question.html', {'question_form': question_form})


@login_required
def question_delete(request,slug):
    question = get_object_or_404(Question,slug = slug)
    question.delete()
    return redirect('question-list')

@login_required
def answer_update(request,id):
    answer = get_object_or_404(Answer,id = id)
    answer_form = AnswerCreateForm(request.POST or None,instance=answer)
    if answer_form.is_valid():
        answer_form.save()
        return redirect('question-details',slug = answer.question.slug)
    return render(request, 'questions/update_answer.html', {'answer_form': answer_form})


@login_required
def answer_delete(request,id):
    answer = get_object_or_404(Answer,id = id)
    answer.delete()
    return redirect('question-details',slug = answer.question.slug)


@login_required
def list_question_answer(request):
    questions = Question.objects.filter(author = request.user).order_by('-created_at')
    answers = Answer.objects.filter(author = request.user).order_by('-created_at')
    return render(request,'questions/list_qus_ans.html',{'questions':questions,'answers':answers})