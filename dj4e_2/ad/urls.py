from django.urls import path
from . import views

app_name='ads'
urlpatterns = [
	path('', views.AdListView.as_view(), name='main'),
	path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad-detail'),
	path('ad/create/', views.AdCreateView.as_view(), name='ad-create'),
	path('ad/<int:pk>/update/', views.AdUpdateView.as_view(), name='ad-update'),
	path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad-delete'),
	path('pic_picture/<int:pk>/', views.stream_file, name='pic_picture'),
]
