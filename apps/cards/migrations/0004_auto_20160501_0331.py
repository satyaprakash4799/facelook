# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20160423_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_created_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_hero_image',
            field=models.ImageField(help_text=b'Add', upload_to=b'/Cards', null=True, verbose_name=b'Card display image', blank=True),
        ),
    ]
