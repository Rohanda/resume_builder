# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length = 40)
    phone = models.CharField(max_length = 13)
    mail = models.EmailField()

    def __str__(self):
        return self.first_name


class Education(models.Model):
    college= models.CharField(max_length=30)
    specialisation = models.CharField(max_length=30)
    Degree = models.CharField(max_length=30)
    grade = models.DecimalField(max_digits=3,decimal_places = 2)
    start_Date = models.DateField(auto_now = False)
    End_Date =  models.DateField(auto_now = False)
    person = models.ForeignKey('Person',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.person.first_name +' Edution'

    class Meta:
        verbose_name_plural = "Education"


class Work(models.Model):
    Company  = models.CharField(max_length=30)
    Position = models.CharField(max_length=30)
    Description = models.TextField(blank = True)
    start_Date = models.DateField(auto_now = False)
    End_Date =  models.DateField(auto_now = False)
    person = models.ForeignKey('Person',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Work"

class Skill(models.Model):
    Name =  models.CharField(max_length=30)
    Description = models.TextField(blank = True)
    person = models.ForeignKey('Person',on_delete=models.CASCADE)


class EducationInline(admin.TabularInline):
    model = Education

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        EducationInline,

    ]



