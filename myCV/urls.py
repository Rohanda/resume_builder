from django.contrib import admin
from myCV import views
from django.conf.urls import url
from django.urls import path
urlpatterns =[
path('',views.person_info,name = 'cvform'),
path('users/',views.users,name = 'submits'),
path('education/<person_id>', views.education_info, name='education_detail'),
path('work/<id>', views.work_info, name='work_detail'),
path('skill/<id>', views.skill_info, name='skill_detail'),
path('update/<idendity>',views.update_cv,name='update'),
path('delete/<idendity>',views.delete_person,name='delete'),



]
