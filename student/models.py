from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Student Name')
    surname = models.CharField(max_length=100, blank=False, null=False, verbose_name='Student Surname')
    email = models.EmailField(verbose_name='Student Email', validators=[EmailValidator])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

