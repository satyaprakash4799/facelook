from django import forms
from .models import UserProfile

class RegForm(forms.ModelForm):
	"""docstring for RegForm"""
	class Meta:
		model= UserProfile
		fields=['email','name']
		
			
