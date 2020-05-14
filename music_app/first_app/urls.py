from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('first',views.first,name='first'),
    path('album_list',views.album_list,name='album_list'),
    path('musician_form',views.musician_form,name='musician_form'),
    path('album_form',views.album_form,name='album_form'),
    path('album_list/<int:artist_id>',views.album_list,name='album_list'),
    path('edit_artist/<int:artist_id>',views.edit_artist,name='edit_artist'),
    path('edit_album/<int:album_id><int:artist_id>',views.edit_album,name='edit_album'),
    path('delete_album/<int:album_id>',views.delete_album,name='delete_album'),
    path('register',views.register,name='register'),
    path('login_1',views.login_1,name='login_1'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('logout_1',views.logout_1,name='logout_1'),
    path('profile',views.profile,name='profile'),

]