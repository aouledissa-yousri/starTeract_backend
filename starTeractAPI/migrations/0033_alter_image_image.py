# Generated by Django 4.0.1 on 2022-02-07 16:41

from django.db import migrations, models
import starTeractAPI.models


class Migration(migrations.Migration):

    dependencies = [
        ('starTeractAPI', '0032_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=starTeractAPI.models.uploadPathImage),
        ),
    ]
