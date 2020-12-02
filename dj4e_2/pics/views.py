from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy 
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad
from .forms import CreateForm
# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView 


class AdListView(ListView):
	model = Ad

class AdDetailView(DetailView):
	model = Ad


class AdCreateView(CreateView):
	model = Ad
	def get(self, request):
		form = CreateForm()
		context = {'form': form}
		return render(request, self.template, context)
def index(request):
	return HttpResponse("I am working properly")