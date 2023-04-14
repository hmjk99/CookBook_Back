# Generated by Django 4.2 on 2023-04-14 16:21

import app_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0011_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=app_api.models.upload_to),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=app_api.models.upload_to),
        ),
    ]