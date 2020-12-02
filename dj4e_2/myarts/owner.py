from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(ListView):
	"Sub class to ListView"

class OwnerDetailView(DetailView):
	"sub class to DetailView"

class OwnerCreateView(LoginRequiredMixin, CreateView):
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
	def get_queryset(self):
		qs = super(OwnerDeleteView, self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
	def get_queryset(self):
		qs = super(OwnerUpdateView, self).get_queryset()
		return qs.filter(owner = self.request.user)