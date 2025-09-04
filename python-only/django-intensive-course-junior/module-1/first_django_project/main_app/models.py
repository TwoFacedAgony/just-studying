from django.db import models

# Create your models here.
class Greeting(models.Model): # the name of table in DB will be main_app_Greeting. this is just a template, not data. data is objects of these classes
    text = models.CharField(max_length=30) # <fieldname> = models.<type_of_field>(<arguments>)
    language = models.CharField(max_length=50)
