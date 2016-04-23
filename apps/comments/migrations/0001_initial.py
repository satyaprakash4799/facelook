# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0002_cards_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(help_text=b'You can give your thoughts for the card.', null=True, verbose_name=b'Comments', blank=True)),
                ('cards', models.ForeignKey(to='cards.Cards')),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
    ]
