from .forms import *
from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
#from .forms import *
# Create your views here.



def post(request):
    pics = Pics_day.objects.all()
    trend = pics.filter(active=True)
    post = Post.objects.all()
    p =[p for p in post]
    c = p[len(p)-1]
    form = WhatForm(request.POST or None)
    watsups = Whatusay.objects.all()
    watsup = watsups.filter(active=True)
    if form.is_valid():
        form.save()
        form = WhatForm()

    ctx = {'form':form,'wat':watsup,'c':c,'tr':trend}
    return render(request, "homepage.html", ctx)


def sermons(request):
    post = AllSongs.objects.all()
    p =[p for p in post]
    c = p[len(p)-1]
    qs = AllSongs.objects.all()
    search = request.GET.get('search')
    if search != '' and search is not None:
            lookups = Q(name__icontains = search) | Q(release__icontains = search)
            qs = AllSongs.objects.filter(lookups)
    paginator = Paginator(qs,2)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    ctx = {'qs':qs,'c':c}
    return render(request, "index.html", ctx)
    


def post_detail(request, pk):
    template_name = 'post_detail.html'
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

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def devotions(request):
    qs = Post.objects.all()
    search = request.GET.get('search')
    if search != '' and search is not None:
            lookups = Q(title__icontains = search) | Q(body__icontains = search) | Q(created__icontains = search)
            qs = Post.objects.filter(lookups)
    
    paginator = Paginator(qs,2)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    user = request.user
    ctx = {'qs':qs, 'user':user}
    print(search)
    return render(request, "devotion.html", ctx)

def sermon_detail(request, pk):
    template_name = 'show.html'
    post = get_object_or_404(AllSongs, pk=pk)
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

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def tryy(request):
    ctx = {}
    return render(request,"show.html",ctx)
