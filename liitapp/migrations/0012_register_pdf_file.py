# Generated by Django 4.2.5 on 2024-03-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liitapp', '0011_alter_register_uploaded_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='media/pdf_files/'),
        ),
    ]