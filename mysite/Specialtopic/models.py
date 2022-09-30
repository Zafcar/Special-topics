from django.db import models
from datetime import datetime


# Name of the class will be the name of the table in sqlite database.
# Each variable created in a class is a column name with the specific datatype.

# This table holds all the student names with there USN.
class Student_database(models.Model):
    Student_name = models.CharField(max_length = 50)
    USN = models.CharField(max_length = 11, primary_key = True)

# This table holds all the student name and the system they used and the in time and out time.
class System_database(models.Model):
    Date = models.DateField(blank=True)
    Student_name = models.CharField(max_length = 50)
    Branch = models.CharField(max_length = 10)
    USN = models.ForeignKey(Student_database, on_delete = models.CASCADE)
    System_no = models.CharField(max_length = 9)
    Time_in = models.TimeField()
    Time_out = models.TimeField()
