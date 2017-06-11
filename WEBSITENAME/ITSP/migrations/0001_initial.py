# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='passwordList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('team_id', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField(default=None)),
                ('member1', models.CharField(max_length=100)),
                ('member2', models.CharField(max_length=100, blank=True)),
                ('member3', models.CharField(max_length=100, blank=True)),
                ('member4', models.CharField(max_length=100, blank=True)),
                ('mentor', models.CharField(max_length=100)),
                ('club', multiselectfield.db.fields.MultiSelectField(max_length=81, choices=[(b'Aeromodelling Club', b'Aeromodelling Club'), (b'Biotech Club', b'Biotech Club'), (b'Electronics And Robotics Club', b'Electronics And Robotics Club'), (b'Web and Coding Club', b'Web and Coding Club')])),
                ('slot', models.CharField(max_length=5, choices=[(b'one', b'One'), (b'two', b'Two')])),
                ('teamPic', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('documentation', models.FileField(upload_to=b'documents/')),
                ('video', models.URLField(max_length=400, null=True, blank=True)),
                ('bill', models.CharField(max_length=100, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
            ],
        ),
    ]
