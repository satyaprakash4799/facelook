# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20160423_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='cards',
            field=models.ForeignKey(default=b'', to='cards.Cards'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments',
            field=models.TextField(default=b'', help_text=b'You can give your thoughts for the card.', verbose_name=b'Comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_profile',
            field=models.ForeignKey(default=b'', to='users.UserProfile'),
        ),
    ]
