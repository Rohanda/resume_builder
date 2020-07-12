# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myCV.models import Person,Education,Work,Skill
from myCV.forms import person_form,education_form,work_form,skill_form
from django.forms import modelformset_factory,inlineformset_factory
from django.views.generic.edit import UpdateView


def index(request):
    return users(request)

def new_cv(request):
    if request.method == 'POST':
        person =person_form(request.POST)
        education = education_form(request.POST)
        work = work_form(request.POST)
        skill= skill_form(request.POST)
        forms = [person,education,work,skill]
        # Check if each form is valid then relate it to person object and save it
        flag = True
        for f in forms:
            if f.is_valid():
                pass
            else :
                flag = False

        if flag == True:
            saved_person = person.save()
            for f in forms[1:]:
                saved_f = f.save(commit = False)
                saved_f.person_id = saved_person.id
                saved_f.save()
            return index(request)

    # TODO: if the form is not valid
    else:
        person =person_form()
        education = education_form()
        work = work_form()
        skill= skill_form()
        form = {'person':person,'education':education,'work':work,'skill':skill}
        return render(request,'builder.html',context =form )

def users(request):
    data = Person.objects.all()
    names = {'all_names': data}
    return render(request,'home.html',context =names )

def build_cv(request):
    formset1 = modelformset_factory(Education,exclude=('person',),extra = 2)
    formset2 = modelformset_factory(Work,exclude=('person',))
    formset3 = modelformset_factory(Skill,exclude=('person',))
    if request.method == 'POST':
        person =person_form (request.POST)
        education = formset1(request.POST)
        work = formset2(request.POST)
        skill = formset3(request.POST)
        forms = [education,work,skill]
        if person.is_valid():
            person.save(commit =False)

        flag = True
        for form in forms:
            for f in form:
                if f.is_valid():
                    pass
                else :
                    flag = False
        if flag == True:
            saved_person = person.save()
            for form in forms:
                for f in form:
                    saved_f = f.save(commit = False)
                    saved_f.person_id = saved_person.id
                    saved_f.save()
            return index(request)
        # TODO: elseif the form is not valid

    else:

        person =person_form()
        education = formset1(queryset=Education.objects.none())
        work = formset2(queryset=Work.objects.none())
        skill = formset3(queryset=Skill.objects.none())
        form = {'person':person,'education':education,'work':work,'skill':skill}
        return render(request,'builder.html',context =form )

def person_info(request,id=-1):
    if id != -1:
        person_inst = Person.objects.get(pk=id)
        person_f = person_form(instance =person_inst )
    else:
        person_f = person_form()
    if request.method == 'POST':
        person_f = person_form(request.POST)
        if person_f.is_valid():
            instance= person_f.save()
            return redirect(education_info,person_id = instance.id)
    form = {'person':person_f}
    return render(request,'builder.html',context =form)

def education_info(request,person_id):
        person_inst = Person.objects.get(pk=person_id)
        education_f = inlineformset_factory(Person,Education,exclude=('person',))
        if request.method == 'POST':
            education_fo = education_f(request.POST,instance = person_inst)
            if education_fo.is_valid():
                education_fo.save()
                return redirect(work_info,id = person_id)
        education_fm = education_f(instance = person_inst)
        form = {'education':education_fm}
        return render(request,'edu.html',context =form)

def work_info(request,id):
    work_f = inlineformset_factory(Person,Work,exclude=('person',))
    person_inst = Person.objects.get(pk=id)
    if request.method == 'POST':
        work_fo = work_f(request.POST,instance = person_inst)
        if work_fo.is_valid():
            work_fo.save()
            return redirect(skill_info,id = id)
    work_fo = work_f(instance = person_inst)
    form = {'work':work_fo}
    return render(request,'work.html',context =form)

def skill_info(request,id):
    skill_f = inlineformset_factory(Person,Skill,exclude=('person',))
    person_inst = Person.objects.get(pk=id)
    if request.method == 'POST':
        skill_fo = skill_f(request.POST,instance = person_inst)
        if skill_fo.is_valid():
            skill_fo.save()
            return index(request)
    form = {'skill':skill_f}
    return render(request,'skill.html',context =form)

def update_person(request,idendity):
    return person_info(request,id = idendity)

def delete_person(request,idendity):
    person_inst = Person.objects.get(pk=idendity)
    person_inst.delete()
    return  index(request)
