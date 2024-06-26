"""
URL configuration for diablo4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from quests import views


urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # Default Page
    path('', TemplateView.as_view(template_name='index.html')),

    path('', views.index, name='index'),
    path('quests/', include('quests.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact', views.contact, name='contact'),
    path('about-us', views.about, name='about'),
]
