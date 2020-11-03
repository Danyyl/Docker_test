from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Status(models.Model):
    status = models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')


class Employees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='Employees')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='Employees')
