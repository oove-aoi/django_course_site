from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ipware import get_client_ip

from django.db.models import Count

from datetime import datetime


from .forms import CustomUserCreationForm, PostCreationForm, PostUpdateForm, CommentCreationForm
from .models import IpAddress, Post, Comment

# Create your views here.
#首頁
def index(request):
	viewcount = get_object_or_404
	post_views_count = Post.objects.annotate(viewer_count=Count('viewersip')).order_by("-viewer_count")
	top_five_of_viewscount = post_views_count[:5]
	
	return render(request, "posts/index.html",{
		"postlist_viewercount": top_five_of_viewscount,

	})

#user相關
def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
		print(form.errors)
	else:
		form = CustomUserCreationForm()

	return render(request, 'users/register.html', {
		'form': form
	})



def userblog(request, user_id):
	blog_owner = get_object_or_404(User, id=user_id)
	blog_post = Post.objects.filter(poster__id=user_id).order_by("-post_time")

	return render(request,'posts/user-blog.html',{
		"blog_owner": blog_owner,
		"posts": blog_post
	})

#post相關

@login_required
def createpost(request):
	if request.method == 'POST':
		form = PostCreationForm(request.POST, request.FILES)
		form.instance.poster = request.user

		posterip, _ = get_client_ip(request)
		if IpAddress.objects.filter(ip=posterip).exists():
			form.instance.posterip = IpAddress.objects.get(ip=posterip)
		else:
			new_ip = IpAddress.objects.get_or_create(ip=ip)
			form.instance.posterip = IpAddress.objects.get(ip=posterip)

		if form.is_valid():
			post = form.save()
			return redirect('index')
		else:
			return False, form.errors
	else:
		form = PostCreationForm()

	return render(request, 'posts/post-CreateAndUpdate.html', {
		'form': form,
		'title': "創建新帖"
	})


def postdetail(request, user_id, slug):
	select_post = get_object_or_404(Post, slug=slug)
	all_comment = Comment.objects.filter(post_id=select_post.id)

	if request.method == 'POST':
		comment_form = CommentCreationForm(request.POST)

		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = select_post
			new_comment.user = request.user
			new_comment.save()
	else:
		comment_form = CommentCreationForm()

		#獲取IP，並判斷是否已經看過這個帖子並依此來決定是否增加觀看數
		#主要參考:https://dev.to/siumhossain/unique-view-count-in-specific-objectview-django-rest-framework-27be
		ip, _ = get_client_ip(request)

		if IpAddress.objects.filter(ip=ip).exists():
			if str(select_post.posterip) != str(ip):
				select_post.viewersip.add(IpAddress.objects.get(ip=ip))
			

		else:
			new_ip = IpAddress.objects.get_or_create(ip=ip)
			select_post.viewersip.add(new_ip)

	return render(request,'posts/post-detail.html',{
		"post": select_post,
		"viewer_count": select_post.get_viewersip_count(),
		"comments": all_comment,
		'comment_form': comment_form,
	})

def updatepost(request, user_id, slug):
	instance = get_object_or_404(Post, slug=slug)

	if request.method == 'POST':
		form = PostUpdateForm(request.POST, request.FILES,instance=instance)
		

		if form.is_valid():
			post = form.save()
			return redirect("post-detail", user_id=user_id, slug=slug)
		else:
			return False, form.errors
	else:
		form = PostUpdateForm(instance=instance)

	return render(request, 'posts/post-CreateAndUpdate.html',{
		'form': form,
		'title': "更新舊帖"
	})

def deletepost(request, user_id, slug):
	post = get_object_or_404(Post, slug=slug)
	post.delete()

	return redirect("user-blog", user_id=user_id)
	

