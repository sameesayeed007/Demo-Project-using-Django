from django import forms
from django.forms import ModelForm
from first_app import models

class MusicianForm(ModelForm):
	class Meta:
		model = models.Musician
		fields = "__all__"



class AlbumForm(ModelForm):
	release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
	class Meta:
		model = models.Album
		fields = "__all__"


