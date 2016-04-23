# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_cards_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='user_profile',
            field=models.ForeignKey(related_name='card', default=b'', to='users.UserProfile'),
        ),
    ]
