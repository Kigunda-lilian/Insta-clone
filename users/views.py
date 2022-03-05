from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registration (request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} successfully!')
    else:
        form =UserCreationForm()
    form=UserCreationForm()
    return render (request, 'users/register.html',{'form':form})