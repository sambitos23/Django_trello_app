from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# ORM
# Object Relational Mapper
# class => Table in DB
# fileds/ attributes => columns in table (This is a part of Django model class)
# object => map to rows in the table

class TaskList(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(
        default=timezone.now
    )
    # user_id, who has created the list?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):   #it is used for name of tasklist in Django Admin
        # return "Hello"
        return f"{self.name}---{self.created_at}"        

# instance of a class is an object
# inherit from the model class provided by the Django
# model is the base class
# Task is the child class

#trello_app_task
class Task(models.Model):   # model class provided my Django, we can reuse this things => connect class to Django
    # in DB => column name, type pf column: VARCHAR(50)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now
    )
    due_date = models.DateTimeField()
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    # ------------------------------------------------
    # this is for python
    # -----------------------------------------------
    # def __init__(self, name, desc, due_date):  # it is the method of initialize attributs in the class
    #     self.name = name       # self refer to that perticular instance of the class
    #     self.desc = desc
    #     self.due_date = due_date
    # ---------------------------------------------------

    def __str__(self):
        return f"{self.name} --- {self.desc}"