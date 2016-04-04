# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_hero_image', models.ImageField(help_text=b'Add', upload_to=b'Cards', null=True, verbose_name=b'Card display image', blank=True)),
                ('card_title', models.CharField(max_length=255)),
                ('card_created_on', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
                ('card_description', models.TextField(verbose_name=b'card_description')),
            ],
            options={
                'verbose_name': 'Cards',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]
