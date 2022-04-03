from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q 
from django.contrib import messages
from .forms import *
from django.template import loader
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage
from django.http import JsonResponse

# Create your views here.
def home(request):
    devotion = Post.objects.all()
    p =[p for p in devotion]
    c = p[len(p)-1]

    sermon = Media.objects.all()
    p =[p for p in sermon]
    serm = p[len(p)-1]

    pics = Pics_day.objects.all()
    trend = pics.filter(active=False)

    pi = Pics_day.objects.all()
    pc =[p for p in pi]
    pic = pc[len(pc)-1]

    form = WhatForm(request.POST or None)
    watsups = Whatusay.objects.all()
    watsup = watsups.filter(active=False)
    if form.is_valid():
        form.save()
        form = WhatForm()


    ctx = {"devotion":c,"sermon":serm,'form':form,'wat':watsup,'tr':trend,'pic':pic}
    return render(request,'homepage.html',ctx)

def devotion(request):
    qs = Post.objects.all()
    search = request.GET.get('search')
    if search != '' and search is not None:
            lookups = Q(title__icontains = search)
            qs = Post.objects.filter(lookups)
    paginator = Paginator(qs,3)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    ctx = {'med':qs}
    return render(request, "index.html", ctx)


def sermon(request):
    med = Media.objects.all()
    search = request.GET.get('search')
    if search != '' and search is not None:
            lookups = Q(name__icontains = search)
            med = Media.objects.filter(lookups)
    paginator = Paginator(med,3)
    page = request.GET.get('page')
    med = paginator.get_page(page)
    ctx = {"med":med}
    print(search)
    return render(request,'sermons.html',ctx)

def devotion_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=False)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    ctx = {'med':post,'new_comment': new_comment,'comment_form': comment_form,'comments': comments}
    return render(request,'devotion.html',ctx)


def sermon_detail(request,pk):
    post = get_object_or_404(Media, pk=pk)
    comments = post.sermon_comments.filter(active=False)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = SermonForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.comment = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    ctx = {'med':post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form}
    return render(request,'sermon.html',ctx)

