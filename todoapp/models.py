from django.db import models

# Create your models here.
#task name
#date
#status

# create table tasks(task_name varchar,date varchar,status varchar)
class Tasks(models.Model):
    task_name=models.CharField(max_length=200)
    date=models.CharField(max_length=120)
    status=models.CharField(max_length=60)