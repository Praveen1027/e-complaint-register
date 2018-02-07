# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class complain(models.Model):
	user=models.ForeignKey(User, default="", help_text='Please enter your username.')
	myname=models.CharField(max_length=50,default='', help_text='Please enter your full name in BlOCK LETTERS')
	enrollment=models.IntegerField(default=0, help_text='Please enter your Enrollment number')
	room=models.CharField(max_length=50,default='', help_text='Enter your room number')
	mobile=models.IntegerField(default=0, help_text='Enter your mobile number')
	date_of_register=models.CharField(max_length=20, default='')
	problem = models.TextField(help_text='Please Enter your problem')
	tag = models.CharField(max_length=50, default="", help_text='Select any given tag for reference')

	def __str__(self):
		return self.problem

	def create_profile(sender, **kwargs):
		if kwargs['created']:
		   user_profile = complain.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile, sender=User)
