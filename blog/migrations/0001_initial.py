# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-06 09:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(default='', help_text='Please enter your full name in BlOCK LETTERS', max_length=50)),
                ('enrollment', models.IntegerField(default=0, help_text='Please enter your Enrollment number')),
                ('room', models.CharField(default='', help_text='Enter your room number', max_length=50)),
                ('mobile', models.IntegerField(default=0, help_text='Enter your mobile number')),
                ('date_of_register', models.CharField(default='', max_length=20)),
                ('problem', models.TextField(help_text='Please Enter your problem')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagone', models.CharField(help_text='Please select any given field', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='complain',
            name='tag',
            field=models.ForeignKey(default=None, help_text='Select any given tag for reference', on_delete=django.db.models.deletion.CASCADE, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='complain',
            name='user',
            field=models.ForeignKey(default='', help_text='Please enter your username.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]