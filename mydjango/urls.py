"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from mydjango.views import home
from app.views import (search_article, create_article, article_details)

from accounts.views import (
    login,
    logout,
    register
)
urlpatterns = [

    path('', home),
    path('articles/', search_article),
    path('articles/create/', create_article),
    path('articles/<int:id>', article_details),

    path('login/', login),
    path('logout/', logout),
    path('register/', register),

    path('admin/', admin.site.urls),

]
