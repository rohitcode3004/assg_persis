from django.forms import ModelForm
from django import forms

from .models import *

class RouterForm(ModelForm):
	class Meta:
		model = Router
		fields = '__all__'
