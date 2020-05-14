from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Musician,Album,userInfo
from first_app import forms
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	
	dic = {'title': "Home Page"}
	return render(request,'first_app/index.html',context=dic)


def first(request):
	musician_list = Musician.objects.order_by("first_name")
	dic = {'title': "Home Page", 'musician_list':musician_list}
	return render(request,'first_app/first.html',context=dic)

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
			return first(request)
	dic = {'title': "Add Musician", 'musician_form': mform}
	return render(request,'first_app/musician_form.html',context=dic)


def album_form(request):
		mform = forms.AlbumForm() #Creating a Musician form object

		if request.method == "POST" :
			mform = forms.AlbumForm(request.POST)

			if mform.is_valid():
				mform.save(commit=True)
				return first(request)
		dic = {'title': "Add Album", 'album_form':mform}
		return render(request,'first_app/album_form.html',context=dic)


def edit_artist(request,artist_id):
	artist_info = Musician.objects.get(pk=artist_id)
	mform = forms.MusicianForm(instance=artist_info) #Creates the form with the existing info
	if request.method == "POST" :
		mform = forms.MusicianForm(request.POST,instance=artist_info)

		if mform.is_valid():
			mform.save(commit=True)
			return album_list(request,artist_id)

	dic = {'title': "Edit Information",'edit_artist':mform}
	return render(request,'first_app/edit_artist.html',context=dic)



def edit_album(request,album_id,artist_id):
	album_info = Album.objects.get(pk=album_id)
	mform = forms.AlbumEForm(instance=album_info) #Creates the form with the existing info
	if request.method == "POST" :
		mform = forms.AlbumEForm(request.POST,instance=album_info)

		if mform.is_valid():
			mform.save(commit=True)
			return album_list(request,artist_id)

	dic = {'title': "Edit Information",'edit_album':mform, 'album_info':album_info}
	return render(request,'first_app/edit_album.html',context=dic)


def delete_album(request,album_id):
	album_deleted = Album.objects.get(pk=album_id).delete()

	dic = {'title':"Album has been deleted" , 'album_deleted' : album_deleted }
	return render(request,'first_app/delete.html',context=dic)

def register(request):
	registered = False 

	if request.method == "POST":
		user_form = forms.UserForm(data = request.POST)
		user_info_form = forms.UserInfoForm(data = request.POST)

		if user_form.is_valid() and user_info_form.is_valid():
			user = user_form.save()
			user.set_password(user.password) #to encrypt the password
			user.save()
			
        
			user_info = user_info_form.save(commit=False)
			user_info.user = user
			if 'profile_pic' in request.FILES:
				user_info.profile_pic = request.FILES['profile_pic']
			user_info.save()
			 # commit false does not save it to database
			#user_info.user = user #connects user and the user_info
			 #checking if the file provided is valid and profile_pic is the field name

			#if 'profile_pic' in request.FILES:
				#user_info.profile_pic = request.FILES['profile_pic']

			#user_info.save()
			#return index(request)
			registered = True

			

	else:
		user_form = forms.UserForm()
		user_info_form = forms.UserInfoForm()









	dic = {'user_form' : user_form , 'user_info_form' : user_info_form, 'registered': registered}
	return render(request,'first_app/register.html',context=dic)

def login_1(request):
	return render(request,'first_app/login.html',context={})



def user_login(request):

	if request.method == "POST":

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('first_app:first'))

			else:
				return HttpResponse("Account is not active")


		else:
			return HttpResponse("Login details are wrong")


	else:
		return render(request,'first_app/register.html',context={})


def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('first_app:logout_1'))



def logout_1(request):
	return render(request,'first_app/logout.html',context={})


def profile(request):
	dic = {}
	if request.user.is_auntheticated:
		current_user = request.user
		user_id = current_user.id
		user_basic_info = User.objects.get(pk=user_id)
		user_more_info = userInfo.objects.get(user__ok=user_id)
		dic = {'user_basic_info': user_basic_info , 'user_more_info': user_more_info}
	return render(request,'first_app/profile.html',context={})





