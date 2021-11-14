from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('create/', views.createRouter, name='create'),
	path('update/<int:pk>/', views.updateRouter, name='update'),
	path('delete/<int:pk>/', views.deleteRouter, name='delete'),
]

