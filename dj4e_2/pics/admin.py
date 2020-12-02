from django.contrib import admin
from .models import Ad
# Register your models here.

class AdAdmin(admin.ModelAdmin):
	exclude = ['picture', 'content_type']

admin.site.register(Ad, AdAdmin)
