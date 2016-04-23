# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='user_profile',
            field=models.ForeignKey(related_name='card', default=1, to='users.UserProfile'),
        ),
    ]
