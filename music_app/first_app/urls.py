from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('album_list',views.album_list,name='album_list'),
    path('musician_form',views.musician_form,name='musician_form'),
    path('album_form',views.album_form,name='album_form'),
    path('album_list/<int:artist_id>',views.album_list,name='album_list'),
]