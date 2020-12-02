from django.urls import path
from . import views



app_name = 'forum'
urlpatterns = [
	path('jsonfun/', views.index, name='jsonfun'),
	path('', views.ForumListView.as_view(), name='main'),
	path('create/', views.ForumCreateView.as_view(), name='forum-create'),
	path('update/<int:pk>/', views.ForumUpdateView.as_view(), name='forum-update'),
	path('<int:pk>/delete/', views.ForumDeleteView.as_view(), name='forum-delete'),
	path('<int:pk>/', views.ForumDetailView.as_view(), name='forum-detail'),
	path('<int:pk>/comment', 
        views.CommentCreateView.as_view(), name='forum-comment-create'),
	path('<int:pk>/comment/delete', views.CommentDeleteView.as_view(), name='comment-delete'),
	path('<int:pk>/like', views.AddLikeView.as_view(), name='forum-like'),
	path('<int:pk>/dislike', views.DeleteLikeView.as_view(), name='forum-dislike'),
]
