# Generated by Django 4.2.5 on 2024-03-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liitapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='desg',
            field=models.CharField(default='', max_length=100),
        ),
    ]
