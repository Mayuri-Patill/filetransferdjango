from django.contrib import admin

from .models import file_upload

class myfile(admin.ModelAdmin):
    fields = ['my_file','file_name']

# Register your models here.


admin.site.register(file_upload,myfile)
