# Generated by Django 2.1.3 on 2019-01-16 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20190116_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_students',
            name='Family_status',
            field=models.CharField(choices=[('FL', 'Fatherless'), ('ML', 'Motherless'), ('PA', 'Parents')], default='PA', max_length=20),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='birthdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 12, 6, 23, 50841)),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='class_attend',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='father',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='mother',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='placeofbirth',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='list_students',
            name='school',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]