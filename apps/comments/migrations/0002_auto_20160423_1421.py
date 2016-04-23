# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='cards',
            field=models.ForeignKey(default=b'', blank=True, to='cards.Cards', null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.TextField(default=b'', help_text=b'You can give your thoughts for the card.', null=True, verbose_name=b'Comments', blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_profile',
            field=models.ForeignKey(default=b'', blank=True, to='users.UserProfile', null=True),
        ),
    ]
