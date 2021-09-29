from django.contrib import admin
from .models import Bookings
from import_export.admin import ImportExportActionModelAdmin
from bookings.models import Bookings
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
# Register your models here.

    

class BookingsAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title','content' ,'created_at', 'updated_at','is_published')
    list_display_links =('id', 'title','content','updated_at')
    search_fields =('id','title','content')


   

admin.site.register(Bookings,BookingsAdmin)



