from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .owner import (
	OwnerListView, 
	OwnerDetailView, 
	OwnerCreateView, 
	OwnerDeleteView,
	OwnerUpdateView)
from .models import Article

class ArticleListView(OwnerListView):
	model = Article
	ordering = ['-created_at']

class ArticleDetailView(OwnerDetailView):
	model = Article


class ArticleCreateView(OwnerCreateView):
	model = Article
	fields = ['title', 'text']
	success_url = reverse_lazy('myarts:article-main')

class ArticleUpdateView(OwnerUpdateView):
	model = Article
	fields = ["title", "text"]
	success_url = reverse_lazy('myarts:article-main')

class ArticleDeleteView(OwnerDeleteView):
	model = Article
	success_url = reverse_lazy('myarts:article-main')


def index(request):
	return HttpResponse("Hi i am index")