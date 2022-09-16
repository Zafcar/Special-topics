from django.contrib import admin
from  django.contrib.auth.models  import  Group

# this import from models.py file which stores all the sql tables.
from .models import Student_database, System_database

# This adds both the tables from models.py into admin site for viewing or adding.
admin.site.register(Student_database)
admin.site.register(System_database)

# Changes the name of the header, title and index.
admin.site.site_title  =  "System Assign Admin"
admin.site.site_header  =  "System Assign Admin" 
admin.site.index_title  =  "Admin Controls"

# Removes all default groups.
admin.site.unregister(Group)

class  detailsAdmin(admin.ModelAdmin):
    list_display=('book_name','category','Author','pages','publisher')