from django.contrib import admin
from .models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
	actions = [csvexport]

admin.site.register(Data)