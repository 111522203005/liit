# Generated by Django 4.2.5 on 2024-03-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liitapp', '0002_register_desg'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='college',
            field=models.CharField(default='', max_length=100),
        ),
    ]
