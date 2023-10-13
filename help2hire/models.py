from django.db import models


class Org(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    ph_num = models.CharField(max_length=10)
    email = models.EmailField(primary_key=True, unique=True, max_length=100)
    address = models.TextField(max_length=200)
    company_name = models.CharField(max_length=50)
    alt_num = models.CharField(max_length=10)
    password = models.CharField(max_length=40)
            


class Seeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True, unique=True)
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=15)
    skills = models.CharField(max_length=50)
    ph_num = models.CharField(max_length=10)
    alt_num = models.CharField(max_length=10)
    dob = models.DateField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    

class Eventlist(models.Model):
    event_id = models.UUIDField(primary_key=True, unique=True)
    org_email = models.EmailField()
    company_name = models.CharField(max_length=100)
    event_title = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    vacancies = models.CharField(max_length=10)
    salary = models.CharField(max_length=10)
    venue = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=10)
    description = models.CharField(max_length=200)


class Job_application(models.Model):
    event_id = models.UUIDField(unique=True, primary_key=True)
    j_email = models.EmailField(max_length=100)
    org_email = models.EmailField(max_length=100)