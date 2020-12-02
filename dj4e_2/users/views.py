from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegisterForm
# Create your views here.
class Register(View):
	template = "users/register.html"
	def get(self, request):
		form = UserRegisterForm()
		context={'form':form}
		return render(request, self.template, context)
	def post(self, request):
		form = UserRegisterForm(request.POST)
		if not form.is_valid():
			context={
			'form':form
			}
			return render(request, self.template, context)
		else:
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username} has been created successfully')
			return redirect(reverse_lazy('login'))