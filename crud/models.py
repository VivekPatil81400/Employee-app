from pyexpat import model
from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)
    emailid = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname

class EmployeeDetail(models.Model):
    EDUCATION = (
        ('Btech', 'BTech'),
        ('Mtech', 'Mtech'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
    )
    id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    education = models.CharField(max_length=6, choices=EDUCATION)
    department = models.CharField(max_length=15)
    salary = models.IntegerField()
    manager = models.CharField(max_length=30)
