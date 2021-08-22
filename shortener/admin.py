from django.contrib import admin
from .models import Url

# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display=(
        'link',
        'uuid'
    )
    search_fields=('link')
    

admin.site.register(Url)