from django.shortcuts import render,redirect,HttpResponse
from .models import Post,Comment
from .forms import postcreate,postedit,AddComment
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


def Post_List(req):
    posts=Post.objects.all()
    return render(req,'index.html',{"posts":posts})

def Register(req):
    if req.method=='POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        password=req.POST.get('password')

        if User.objects.filter(email=email):
            messages.error(req,"Email Already Exist")
            return redirect('Register')
        else:
            User.objects.create(
                username=username,
                email=email,
                password=password
            )
            messages.success(req,"Successfully Registered")
            return redirect('/')
    else:
        return render(req,'Register.html')


def Login(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.error(req,'Invalid Credential')
            return redirect('Login')
    else:
        return render(req,'Login.html')    

def logout(req):
    auth.logout(req)
    return redirect('/')


def CreatePost(req):
    if req.method=='POST':
        form=postcreate(req.POST,req.FILES)
        if form.is_valid():
            Post=form.save(commit=False)
            Post.author=req.user
            Post.save()
            messages.success(req,'post created successsfully')
            return redirect('/')
        else:
            messages.error(req,'invalid form data')
            return render(req,'createpost.html',{'form':form})

    else:
        form=postcreate()
        return render(req,'createpost.html',{'form':form})


def allpost(req):
    x=req.user
    posts=Post.objects.filter(author__username=x.username)
    return render(req,'AllPost.html',{"posts":posts})

def deletepost(req,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('allpost')

def editpost(req,post_id):
    post=Post.objects.get(id=post_id)
    if req.method=='POST':
       form=postedit(req.POST,req.FILES,instance=post)
       if form.is_valid():
            form.save()
            return redirect('allpost')
    else:
        form=postedit(instance=post)

    return render(req,'EditPost.html',{'form':form ,'post':post})

@login_required
def addcomment(req,post_id):
    post=Post.objects.get(id=post_id)

    if req.method=='POST':
        form=AddComment(req.POST)
        if form.is_valid():
            Comment=form.save(commit=False)
            Comment.post=post
            Comment.author=req.user
            Comment.save()
            return redirect('/')
        
    else:
        form=AddComment()
    return render(req,'AddComment.html',{'form':form,'post':post})


def viewcomment(req,post_id):
    comments=Comment.objects.filter(post__id=post_id)
    comment_count=comments.count()
    return render(req,'Comments.html',{'comments':comments,'comment_count':comment_count})
