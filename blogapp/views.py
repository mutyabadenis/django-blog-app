from django.shortcuts import render, redirect
from .models import Blogapp
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.
def article_details(request,slug):
   #return HttpResponse(slug)
   article = Blogapp.objects.get(slug=slug)
   return render(request, 'blogapp/article_detail.html',{'article':article})


articles = Blogapp.objects.all().order_by('date')

def about(request):
    return render(request, 'blogapp/about.html')

def home(request):
    return render(request, 'blogapp/home.html')

def blog_list(request):
    return render(request,'blogapp/articles.html',{'articles':articles} )

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreatedArticle(request.POST,request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blogapp:articlelist')
    else:
      form = forms.CreatedArticle
    return render(request,'blogapp/create.html',{'form':form})
