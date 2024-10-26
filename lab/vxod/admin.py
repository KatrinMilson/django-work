from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(Book_read)
admin.site.register(Reader)