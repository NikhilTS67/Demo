# Generated by Django 4.1.7 on 2023-02-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-06-22'),
            preserve_default=False,
        ),
    ]
