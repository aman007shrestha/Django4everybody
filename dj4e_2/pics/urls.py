from django.urls import path, reverse_lazy
from . import views

app_name='pics'
urlpatterns = [
#	path('', views.index, name="view"),
	path('', views.AdListView.as_view(), name='ad-list'),
	path('pic/<int:pk>/',views.AdDetailView.as_view(), name='ad-detail'),
	path('pic/create/', views.AdCreateView.as_view(success_url=reverse_lazy('pics:ad-list'), name='ad-create'),
	path('pic/<int:pk>/update/', views.AdUpdateView.as_view(success_url=reverse_lazy('pics:ad-list')), name='ad-update'),
	path('pic/<int:pk>/delete/', views.AdDeleteView.as_view(success_url=reverse_lazy('pics:ad-list')), name='ad-delete'),
	path('pic_picture/<int:pk>/', views.stream_file, name='ad-picture'),

	]
