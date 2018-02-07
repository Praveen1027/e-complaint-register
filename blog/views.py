# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import complain
from .forms import complainForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def post_list(request):
    if request.method == 'POST':
        form = complainForm(request.POST)
        if form.is_valid():
            obj = complain()
            obj.user_id = request.user.id
            obj.myname = form.cleaned_data['myname']
            obj.enrollment = form.cleaned_data['enrollment']
            obj.room = form.cleaned_data['room']
            obj.mobile = form.cleaned_data['mobile']
            obj.date_of_register = form.cleaned_data['date_of_register']
            obj.problem = form.cleaned_data['problem']
            obj.tag = form.cleaned_data['tag']
            obj.save()
            return HttpResponseRedirect("comp/")


    else:
        form = complainForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def comp(request) :
    return render(request, 'blog/comp.html')
