# Generated by Django 3.2.9 on 2021-11-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
