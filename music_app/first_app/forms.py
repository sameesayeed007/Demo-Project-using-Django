from django import forms
from django.forms import ModelForm
from first_app import models
from django.contrib.auth.models import User

class MusicianForm(ModelForm):
	class Meta:
		model = models.Musician
		fields = "__all__"



class AlbumForm(ModelForm):
	release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
	class Meta:
		model = models.Album
		fields = "__all__"

class AlbumEForm(ModelForm):
	release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
	class Meta:
		model = models.Album
		fields = ['name', 'release_date', 'num_stars']

class UserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'password', 'email']

class UserInfoForm(ModelForm):
	class Meta:
		model = models.userInfo
		fields = ['facebook_id','profile_pic']
