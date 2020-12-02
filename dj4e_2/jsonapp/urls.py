from django.urls import path
from . import views
import os
from django.views.static import serve
from django.conf.urls import url


app_name = "jsonapp"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
urlpatterns = [
	path('', views.index, name='main'),
	path('check', views.check, name="check"),
	path('talk', views.TalkMain.as_view(), name='talk'),
	path('messages', views.TalkMessages.as_view(), name='messages'),
	url(r'static/(?P<path>.*)$', serve, 
		{'document_root': os.path.join(BASE_DIR, 'static'), 'show_indexes': True},
		name='static'
		),
]