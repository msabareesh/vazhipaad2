"""vazhipaad1 URL Configuration

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
from django.urls import path
from .views import (
    TempleListView,
    TempleDetailView,
    TempleCreateView,
    TempleUpdateView,
    TempleDeleteView
)
app_name = 'temples'
urlpatterns = [
    path('', TempleListView.as_view(), name='Temple-List'),
    path('<int:id>/', TempleDetailView.as_view(), name='Temple-Details'),
    path('<int:id>/update/', TempleUpdateView.as_view(), name='Temple-Update'),
    path('create/', TempleCreateView.as_view(), name='Temple-Create'),
    path('<int:id>/delete/', TempleDeleteView.as_view(), name='Temple-Delete'),
]
