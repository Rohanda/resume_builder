# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.forms import CVform
from django.shortcuts import render

# # Create your views here.
# def PersonalInfo(request):
#     if request.method == 'POST':
#         # Populate the form with the data in the request
#         form = CVform(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thanks/')
#     else:
#         # Make the form empty
#         form = CVform()
# return render(request, context = {'form': form})