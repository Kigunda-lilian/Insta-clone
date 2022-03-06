from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Comment, Like
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, AddPostForm
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='login/')
def home(request):
    posts = Image.objects.all().order_by('-id')
    users = Profile.objects.all()
    form = CommentForm()
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            commentt = form.save(commit=False)
            commentt.user = request.POST.user
            commentt.save()
            return redirect('home')
            
    return render(request, 'instagram/home.html',{"posts":posts,  "form":form, 'users':users})

def search_results(request):
    
    if 'posts' in request.GET and request.GET["posts"]:
        search_term = request.GET.get("posts")
        searched_posts = Image.search_by_name(search_term)
        message = search_term

        return render(request, 'instagram/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You have not searched for any term"
        return render(request, 'instagram/search.html',{"message":message})