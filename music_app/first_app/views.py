from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms
from django.db.models import Avg
# Create your views here.
def index(request):
	musician_list = Musician.objects.order_by("first_name")
	dic = {'title': "Home Page", 'musician_list':musician_list}
	return render(request,'first_app/index.html',context=dic)

def album_list(request,artist_id):
	artist_info = Musician.objects.get(pk=artist_id)
	album_list = Album.objects.filter(artist=artist_id).order_by('name')
	artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
	dic = {'title': "List of Albums",'artist_info': artist_info, 'album_list':album_list,'artist_rating':artist_rating}
	return render(request,'first_app/album_list.html',context=dic)


def musician_form(request):
	mform = forms.MusicianForm() #Creating a Musician form object

	if request.method == "POST" :
		mform = forms.MusicianForm(request.POST)

		if mform.is_valid():
			mform.save(commit=True)
			return index(request)
	dic = {'title': "Add Musician", 'musician_form': mform}
	return render(request,'first_app/musician_form.html',context=dic)


def album_form(request):
		mform = forms.AlbumForm() #Creating a Musician form object

		if request.method == "POST" :
			mform = forms.AlbumForm(request.POST)

			if mform.is_valid():
				mform.save(commit=True)
				return index(request)
		dic = {'title': "Add Album", 'album_form':mform}
		return render(request,'first_app/album_form.html',context=dic)
