from django.contrib import admin
from .models import Free_Download

# Register your models here.
class FreeDownloadAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'file',
        'author',
        'created_on'
    )


admin.site.register(Free_Download, FreeDownloadAdmin)