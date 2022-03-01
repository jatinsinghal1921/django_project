import imp
from django.shortcuts import redirect, render
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import postForm
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import SuspiciousOperation


def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, "blog/home.html", {"page_obj": page_obj})


def detailBlog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/blogDetail.html", {'post': post})


@ login_required(login_url='login')
def createBlog(request):
    if request.method == "POST":
        postFormObj = postForm(request.POST)
        if postFormObj.is_valid():
            postFormObj.instance.author = request.user
            postFormObj.save()
            return redirect(reverse('blog-detail', kwargs={'pk': postFormObj.instance.id}))
    else:
        postFormObj = postForm()
    return render(request, "blog/blogCreate.html", {'form': postFormObj})


@ login_required(login_url='login')
def updateBlog(request, pk):
    postObj = get_object_or_404(Post, pk=pk)
    if(postObj.author != request.user):
        raise PermissionDenied()
    if request.method == "POST":
        postFormObj = postForm(request.POST, instance=postObj)
        if postFormObj.is_valid():
            postFormObj.save()
            return redirect(reverse('blog-detail', kwargs={'pk': postObj.id}))
    else:
        postFormObj = postForm(instance=postObj)
    return render(request, "blog/blogUpdate.html", {'form': postFormObj})


@ login_required(login_url='login')
def deleteBlog(request, pk):
    postObj = get_object_or_404(Post, pk=pk)
    if(postObj.author != request.user):
        raise PermissionDenied()
    if request.method == "POST":
        postObj.delete()
        return redirect("blog-home")
    return render(request, "blog/blogDelete.html", {'postObj': postObj})


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
