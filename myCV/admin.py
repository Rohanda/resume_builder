# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Person,Education,Work,Skill


# Register your models here.


class EducationInline(admin.TabularInline):
   model = Education
class WorkInline(admin.TabularInline):
   model = Work
class SkillInline(admin.TabularInline):
   model = Skill

class PersonAdmin(admin.ModelAdmin):
   
    inlines = [
        EducationInline,
        WorkInline,
        SkillInline,

    ]



admin.site.register(Person,PersonAdmin)
#admin.site.register(Education)
#admin.site.register(Work)
#admin.site.register(Skill)