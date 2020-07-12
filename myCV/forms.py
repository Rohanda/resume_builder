from django import forms
from .models import Person,Education,Work,Skill

class person_form(forms.ModelForm):
    class Meta:
        model = Person
        exclude = '__all__'

class education_form(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('person',)

class work_form(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ('person',)

class skill_form(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ('person',)
