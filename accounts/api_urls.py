from django.urls import path

from accounts.views import *

	
urlpatterns = [
	path('home/', RouterAPIView.as_view()),
	path('home/<int:id>', RouterDetailView.as_view()),

]

