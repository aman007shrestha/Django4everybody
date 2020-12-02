from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View 
from django.views.generic import (
	CreateView,
	UpdateView,
	DetailView,
	DeleteView,
	ListView
	)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Ad
from django.http import HttpResponse
from .forms import CreateForm
# Create your views here.


class AdListView(ListView):
	model = Ad

class AdDetailView(DetailView):
	model = Ad

class AdCreateView(LoginRequiredMixin, View):
	template_name = 'ad/ad_form.html'
	success_url = reverse_lazy('ads:main')

	def get(self, request):
		form = CreateForm()
		context = {
		'form': form
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = CreateForm(request.POST, request.FILES or None)

		if not form.is_valid():
			context = {
			'form':form
			}
			return render(request, self.template_name, context)
		print("This ran")
		form.instance.owner = self.request.user
		print('1')
		form.save()
		print('6')
		return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin, View):
	template_name = 'ad/ad_form.html'
	success_url = reverse_lazy('ads:main')
	def get(self, request, pk):
		ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
		form = CreateForm(instance = ad)
		context = {
		'form': form
		}
		return render(request, self.template_name, context)

	def post(self, request, pk):
		ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
		form = CreateForm(request.POST, request.FILES or None, instance=ad)

		if not form.is_valid():
			ctx = {'form': form}
			return render(request, self.template_name, ctx)
		print('1')
		print(type(form.instance))
		# <class 'ad.models.Ad'>

		form.save()

		

		return redirect(self.success_url)



class AdDeleteView(DeleteView):
	model = Ad
	success_url = reverse_lazy('ads:main')
	def get_queryset(self):
		qs = super(AdDeleteView, self).get_queryset()
		return qs.filter(owner=self.request.user)



def stream_file(request, pk):
	ad = get_object_or_404(Ad, id=pk)
	response = HttpResponse()
	response['Content-Type'] = ad.content_type
	response['Content-Length'] = len(ad.picture)
	response.write(ad.picture)
	return response