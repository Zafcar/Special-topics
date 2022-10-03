from django.db import models
from datetime import datetime

#new commit here
# Name of the class will be the name of the table in sqlite database.
# Each variable created in a class is a column name with the specific datatype.

# This table holds all the student names with there USN.
class Student_database(models.Model):
    Student_name = models.CharField(max_length = 50)
    USN = models.CharField(max_length = 11)

# This table holds all the student name and the system they used and the in time and out time.
class System_database(models.Model):
    Date = models.DateField(auto_now_add=True, blank=True)
    Student_name = models.CharField(max_length = 50)

    courses=(
        ('cs','CSE'),
        ('ec','ECE'),
        ('as','ASE'),
        ('me','Mech')
        
    )
    Branch = models.CharField(choices=courses,max_length = 10)
    USN = models.CharField(max_length = 11)

    systems=(
        ('s1','System1'),
        ('s2','System2'),
        ('s3','System3'),
        ('s4','System4'),
        ('k1','Kindle1'),
        ('k2','Kindle2')
    )
    System_no = models.CharField(choices=systems,max_length = 9)
    Time_in = models.TimeField()
    Time_out = models.TimeField()