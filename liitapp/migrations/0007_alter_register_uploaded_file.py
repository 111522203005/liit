# Generated by Django 4.2.5 on 2024-03-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liitapp', '0006_rename_designation_register_designation1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='uploaded_file',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
    ]
