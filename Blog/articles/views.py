from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Articles
from .forms import LoginForm,UserRegistrationForm,ArticleCreateForm,ArticleUpdateForm
from django.contrib.auth import login,authenticate
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required


def article_list(request):
    article_list = Articles.objects.all().order_by('-published')
    paginator = Paginator(article_list,3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,'article.html',{'article_list':articles,'page':page})


def article_details(request,slug):
    article = get_object_or_404(Articles,slug = slug)
    return render(request,'details.html',{'article':article})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                login(request,user)
                return HttpResponse('AUTHENTICATED')
            else:
                return HttpResponse('INVALID USER')

    else:
        form = LoginForm()
    print("form",form)
    return render(request,'account/login.html',{'form':form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/register_done.html',{'user_form':user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})


@login_required
def article_form(request):
    if request.method == 'POST':
        article_form = ArticleCreateForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        article_form = ArticleCreateForm()
    return render(request,'account/add_article.html',{'article_form':article_form})


def article_update(request,slug):
    article = get_object_or_404(Articles,slug=slug)
    article_form = ArticleUpdateForm(request.POST or None,instance = article)
    if article_form.is_valid():
        article_form.save()
        return redirect('article_list')
    else:
        return render(request,'account/add_article.html',{'article_form':article_form})

def article_delete(request,slug):
    article = get_object_or_404(Articles,slug =slug)
    article.delete()
    return redirect('article_list')