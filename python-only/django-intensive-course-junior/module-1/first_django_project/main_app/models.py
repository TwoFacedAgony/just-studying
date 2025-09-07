from django.db import models
from django.utils.timezone import now

# Create your models here.
class Greeting(models.Model): # the name of table in DB will be main_app_Greeting. this is just a template, not data. data is objects of these classes
    text = models.CharField(max_length=30) # <fieldname> = models.<type_of_field>(<arguments>)
    language = models.CharField(max_length=50)

class Person(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    photo = models.ImageField()
    is_employed = models.BooleanField(default=False)
    height = models.DecimalField(max_digits=3, decimal_places=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.URLField()


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Event(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateField(default=now) #uses current data if not set by user
    count = models.PositiveSmallIntegerField()


class LogEntry(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    CHOICES = (
        (1, 'Плохо'),
        (2, 'Неудовлетворительно'),
        (3, 'Удовлетворительно'),
        (4, 'Хорошо'),
        (5, 'Отлично'),)

    text = models.TextField(max_length=2000)
    rating = models.PositiveSmallIntegerField(choices=CHOICES)

    def __str__(self):
        return f'Оценка: {self.rating}. Отзыв: {self.text}'


# many-to-one
class Faculty(models.Model):
    title = models.CharField(max_length=100)


class StudentFaculty(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    faculty = models.ForeignKey(Faculty, on_delete = models.SET_NULL, null=True)


