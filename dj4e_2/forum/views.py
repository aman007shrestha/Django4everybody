from django.shortcuts import render, get_object_or_404, redirect
from myarts.owner import (
	OwnerListView,
	OwnerCreateView,
	OwnerUpdateView,
	OwnerDeleteView,
	OwnerDetailView,
	)
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CommentForm
from .models import Forum, Comment, Like
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def index(request):
	stuff={
	"first": "This is firist",
	"second": "This is second"
	}
	return JsonResponse(stuff)

class ForumListView(OwnerListView):
	model = Forum
	template_name = "forum/forum_list.html"

	def get(self, request):
		forum_list=Forum.objects.all()
		liked_forum = list()
		if request.user.is_authenticated:
			rows = request.user.likes_forum.values('id')
			#  rows of id of liked forum
			likes = [row['id'] for row in rows]
		ctx = {
			'forum_list' : forum_list,
			'likes': likes,
		}
		return render(request, self.template_name, ctx)


class ForumCreateView(OwnerCreateView):
	model = Forum
	fields = ['title', 'text']
	success_url = reverse_lazy('forum:main')


class ForumUpdateView(OwnerUpdateView):
	model = Forum
	fields = ['title', 'text']
	success_url = reverse_lazy('forum:main')

class ForumDeleteView(OwnerDeleteView):
	model = Forum
	success_url = reverse_lazy('forum:main')

class ForumDetailView(OwnerDetailView):
	model = Forum
	template_name = "forum/forum_detail.html"

	def get(self, request, pk):
		f = get_object_or_404(self.model, id=pk)
		comments = Comment.objects.filter(forum=f).order_by('-updated_at')
		comment_form = CommentForm()
		context = {
		'forum':f, 
		'comments':comments, 
		'comment_form':comment_form,
		}
		return render(request, self.template_name, context)


class CommentCreateView(LoginRequiredMixin, View):
	def post(self, request, pk):
		f = get_object_or_404(Forum, id=pk)
		comment_text = Comment(text=request.POST['comment'], owner=request.user, forum=f)
		comment_text.save()
		return redirect(reverse('forum:forum-detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
	model = Comment
	def get_success_url(self, request):
		forum = self.object.forum
		return reverse('forums:forum-detail', args=[forum.id])

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


@method_decorator(csrf_exempt, name='dispatch')
class AddLikeView(LoginRequiredMixin, View):
	def post(self, request, pk):
		f = get_object_or_404(Forum, id=pk)
		liked_objects = Like(owner=request.user, forum=f)
		try:
			liked_objects.save()
		except IntegrityError as e:
			pass
		return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteLikeView(LoginRequiredMixin, View):
	def post(self, request, pk):
		f = get_object_or_404(Forum, id=pk)
		try:
			Like.objects.get(owner=request.user, forum=f).delete()
		except Like.DoesNotExist as e:
			pass
		return HttpResponse()

