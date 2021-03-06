"""dj4e URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
import os
from django.views.static import serve


urlpatterns = [
	path('', include('home.urls')),
    path('myarts/', include('myarts.urls')),
    path('ads/', include('ad.urls')),
    path('forum/', include('forum.urls')),
    path('jsonapp/', include('jsonapp.urls')),
    # path('pics/', include('pics.urls')), replaced by ad app
    path('admin/', admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('register/', user_views.Register.as_view(), name="register"),
]
# server favicon
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
            "path":"favicon.ico",
            "document_root": os.path.join(BASE_DIR, "home/static"),
        } 
        ),

]
