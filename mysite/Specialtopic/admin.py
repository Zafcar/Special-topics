from django.contrib import admin

# this import from models.py file which stores all the sql tables.
from .models import Student_database, System_database

# This adds both the tables from models.py into admin site for viewing or adding.
admin.site.register(Student_database)
admin.site.register(System_database)
