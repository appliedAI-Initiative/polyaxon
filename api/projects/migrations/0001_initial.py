# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PolyaxonSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('content', models.TextField(help_text='The yaml content of the polyaxonfile/specification.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(help_text='Name of the project.', max_length=256)),
                ('description', models.TextField(blank=True, help_text='Description of the project.', null=True)),
                ('is_public', models.BooleanField(default=True, help_text='If project is public or private.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='polyaxonspec',
            name='project',
            field=models.ForeignKey(help_text='The project this polyaxonfile belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='polyaxonspec',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to=settings.AUTH_USER_MODEL),
        ),
    ]
