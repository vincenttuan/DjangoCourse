"""DjangoCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from DjangoCourse import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('hello/<str:name>/', views.hello_name),
    path('hello/<str:op>/<int:x>/<int:y>/', views.hello_op),
    path('page/users/', views.page_users),
    path('page/polls/', views.page_polls),
    path('page/<str:name>/', views.page_user),
    path('page/bmi/<str:name>/', views.page_bmi),
    path('form/profile', views.form_profile),
    path('form/profile/model', views.form_profile_model),
    path('form/twii', views.form_twii),
    path('twii/getcsv', views.twii_getcsv),
    path('crud/music', views.crud_music),
    path('api/', include(router.urls)),
    path('rest/music', views.rest_music),
]
