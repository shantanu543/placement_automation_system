from __future__ import unicode_literals
from django.db import models
from time import time
from django.contrib.auth.models import User


def get_upload_filename(instance,filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)


def get_upload_imagename(instance,filename):
    return "credentials/dist/img/%s" % (filename)
# Create your models here.

class PLACEMENTS_DATA(models.Model):
    totalstudents=models.IntegerField(null=True,default=0)
    totalpercentageplaced=models.IntegerField(null=True,default=0)
    totalpostgraduate=models.IntegerField(null=True,default=0)
    undergradplaced=models.IntegerField(null=True,default=0)
    totalundergraduate=models.IntegerField(null=True,default=0)
    postgradplaced=models.IntegerField(null=True,default=0)

class contact(models.Model):
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=40)
    mobile=models.IntegerField(null=True)
    temporary_address=models.CharField(max_length=50)
    permanent_address=models.CharField(max_length=50,null=True)
    website=models.CharField(max_length=20)
    upload_cv=models.FileField(upload_to='cvfiles')
   
class internship(models.Model):
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=40)
    field1=models.CharField(max_length=200,null=True)
    field2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200,null=True)
    
class postgrad(models.Model):
    username=models.CharField(max_length=20)
    year_of_passing=models.IntegerField()
    Last_spi=models.FloatField(max_length=10)
    Cpi=models.FloatField(max_length=10)
    Branch_of_study=models.CharField(max_length=20)

class undergrad(models.Model):
    username=models.CharField(max_length=20)
    year_of_passing=models.IntegerField()
    Last_spi=models.FloatField(max_length=10)
    Cpi=models.FloatField(max_length=10)
    Branch_of_study=models.CharField(max_length=20)

class srsec(models.Model):
    username=models.CharField(max_length=20)
    year_of_passing=models.IntegerField()
    percentage_obtained=models.FloatField(max_length=10)
    school=models.CharField(max_length=40)
    Board=models.CharField(max_length=20)
    
class sec(models.Model):
    username=models.CharField(max_length=20)
    year_of_passing=models.IntegerField()
    percentage_or_cpi=models.FloatField(max_length=10)
    school=models.CharField(max_length=40)
    Board=models.CharField(max_length=20)
    
class language(models.Model):
    username=models.CharField(max_length=20)
    languages_known=models.CharField(max_length=40)   
    
class project(models.Model):
    username=models.CharField(max_length=20)
    project1=models.CharField(max_length=200,null=True)
    project2=models.CharField(max_length=200)
    project3=models.CharField(max_length=200,null=True)
    
class photo(models.Model):
    username=models.CharField(max_length=20)
    imagename=models.CharField(max_length=50,null=True)
    upload=models.ImageField(upload_to=get_upload_imagename,null=True)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    
####################    
##company models###
###################

class overview(models.Model):
    username=models.CharField(max_length=20)
    description=models.CharField(max_length=500,null=True)
    url=models.CharField(max_length=20,null=True)
    
    
class jobprofile(models.Model):
    username=models.CharField(max_length=20)
    position=models.CharField(max_length=20,null=True)
    CPI_cut_off=models.FloatField(max_length=10)
    Branches=models.CharField(max_length=500,null=True)
    description=models.CharField(max_length=500,null=True)
    
class benefits(models.Model):
    username=models.CharField(max_length=20)
    description=models.CharField(max_length=500,null=True)
    
class statistics(models.Model):
    username=models.CharField(max_length=20)
    description=models.CharField(max_length=500,null=True)
    
class logo(models.Model):
    username=models.CharField(max_length=20)
    upload=models.ImageField(upload_to=get_upload_imagename,null=True)
    

class media(models.Model):
    username=models.CharField(max_length=20)
    upload=models.ImageField(upload_to=get_upload_imagename,null=True)
    
class headoffice(models.Model):
    username=models.CharField(max_length=20)
    plot_number=models.CharField(max_length=30,null=True)
    Area=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=30,null=True)
    Pincode=models.IntegerField(null=True)
    Country=models.CharField(max_length=30,null=True)
    Phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=30)
    
class Work(models.Model):
    username=models.CharField(max_length=20)
    plot_number=models.CharField(max_length=30,null=True)
    Area=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=30,null=True)
    Pincode=models.IntegerField(null=True)
    Country=models.CharField(max_length=30,null=True)
    Phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=30)
    
class Sales_office(models.Model):
    username=models.CharField(max_length=20)
    plot_number=models.CharField(max_length=30,null=True)
    Area=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=30,null=True)
    Pincode=models.IntegerField(null=True)
    Country=models.CharField(max_length=30,null=True)
    Phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=30)