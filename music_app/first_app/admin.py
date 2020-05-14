from django.contrib import admin
from first_app.models import Musician,Album,userInfo

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(userInfo)