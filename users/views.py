from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from .forms import UserRegisterForm
def registration (request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect ('home')
    else:
        form =UserRegisterForm()
    form=UserRegisterForm()
    return render (request, 'users/register.html',context={'form':form})