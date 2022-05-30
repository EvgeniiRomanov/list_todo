"""test_blog URL Configuration

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
from django.urls import path
from . import views     # . значит с данного приложения, за его пределы не лезем


urlpatterns = [
    #path('datetime/', views.SimpleView.as_view()),
    #path('blog_new/', views.SimpleView.as_view()),
    #path('login/', views.SimpleView.as_view()),
    path('notes/', views.SimpleView.as_view()),
    #path('notes/<int:pk>', views.NoteDetailAPIView.as_view()), # int регулярка
    #path('notes/public/', views.PublicNoteListAPIView.as_view())

]
