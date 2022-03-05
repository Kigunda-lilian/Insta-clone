from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from .forms import UserRegisterForm
def registration (request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You are now able to login')
            return redirect ('login')
    else:
        form =UserCreationForm()
    form=UserCreationForm()
    return render (request, 'users/register.html',context={'form':form})

def profile(request):
    return render (request,'users/profile.html')