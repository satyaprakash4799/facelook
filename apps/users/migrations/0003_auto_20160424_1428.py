# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160424_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name': 'UserProfileInfo', 'verbose_name_plural': 'UserProfileInfo'},
        ),
    ]
