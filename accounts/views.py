from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def login_views(request):
   if request.method == 'POST':
     form = AuthenticationForm(data=request.POST)
     if form.is_valid():
        user = form.get_user()
        login(request,user)
        if 'next' in request.POST:
           return redirect(request.POST.get('next'))
        else:
           return redirect('blogapp:articlelist')
   else:
      form = AuthenticationForm()
   return render(request, 'accounts/login.html', {'form':form})     
       
   



def signup_views(request):
   if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
       user = form.save()
       login(request,user)
        #login user
       return redirect('blogapp:articlelist')
   else:
     form = UserCreationForm()
   return render(request, "accounts/signup.html", {'form':form})

def logout_views(request):
   if request.method == 'POST':
      logout(request)
      return redirect('blogapp:articlelist')