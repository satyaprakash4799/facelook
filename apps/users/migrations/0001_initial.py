# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('joining_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date Joined')),
                ('user', models.OneToOneField(verbose_name=b'related user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=8, choices=[(b'Others', b'Others'), (b'Male', b'Male'), (b'Female', b'Female')])),
                ('full_name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('profile_picture', models.ImageField(upload_to=b'uploaded_files')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfileInfo',
                'verbose_name_plural': "UserProfileInfo's",
            },
        ),
    ]
