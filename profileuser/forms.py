from django.forms import ModelForm
from django import forms
from profileuser.models import Profile

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['real_name','surname','bio','main_photo']