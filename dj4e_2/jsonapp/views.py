from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Message
from django.contrib.humanize.templatetags.humanize import naturaltime
import time

# Create your views here.
def index(request):
	time.sleep(2)
	stuff={
	"first": "This is firist",
	"second": "This is second"
	}
	return JsonResponse(stuff)

class TalkMain(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'jsonapp/talk.html')

	def post(self, request) :
		message = Message(text=request.POST['message'], owner=request.user)
		message.save()
		return redirect(reverse('jsonapp:talk'))


class TalkMessages(LoginRequiredMixin, View) :
	def get(self, request):
		messages = Message.objects.all().order_by('-created_at')[:10]
		results = []
		for message in messages:
			result = [message.text, naturaltime(message.created_at), message.owner.username]
			results.append(result)
		return JsonResponse(results, safe=False)


def check(request):
	return render(request, "jsonapp/check.html")
