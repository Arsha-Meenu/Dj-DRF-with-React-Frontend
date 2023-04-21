from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from apps.articles.forms import LoginForm,UserRegistrationForm
from .forms import ProfileForm
from django.contrib.auth import login,authenticate
from apps.articles.models import Articles
from apps.questions.models import Question
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        print('UserRegistrationForm',UserRegistrationForm)
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'articles/account/register_done.html',{'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request,'articles/account/register.html',{'user_form':user_form})


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,username = cd['username'],password = cd['password'])
#             if user is not None:
#                 login(request,user)
#                 article = Articles.objects.filter(author=request.user).values('slug').first()
#                 print('art: ',article)
#                 question = Question.objects.filter(author=request.user).values('slug').first()
#                 return render(request,'questions/question_details.html',{'article':article,'question':question})
#             else:
#                 return HttpResponse('INVALID USER')
#
#     else:
#         form = LoginForm()
#     return render(request,'registration/login.html',{'form':form})



@login_required
def profile_change(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile has been updated.')

    form = ProfileForm(instance=request.user)
    return render(request,'registration/profile.html',{'form':form})


def profile_redirect(request):
    return render(request,'registration/profile_redirect.html')
