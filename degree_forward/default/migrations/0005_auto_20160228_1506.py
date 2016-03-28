# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-28 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_auto_20160225_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degreesem',
            name='Degree',
        ),
        migrations.RemoveField(
            model_name='degreesem',
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='semclass',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='semclass',
            name='Semester',
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem1', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem2', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem3', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem4', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem5', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem6', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem7', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='degreeplan',
            name='Semester8',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sem8', to='default.Semester'),
        ),
        migrations.AddField(
            model_name='semester',
            name='Classes',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='DegreeSem',
        ),
        migrations.DeleteModel(
            name='SemClass',
        ),
    ]