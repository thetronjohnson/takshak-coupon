from django.contrib import admin
from .models import Data
from csvexport.actions import csvexport
# Register your models here.

class DataAdmin(admin.ModelAdmin):
	actions = [csvexport]

admin.site.register(Data)