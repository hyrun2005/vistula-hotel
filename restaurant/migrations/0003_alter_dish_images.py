# Generated by Django 5.1.2 on 2024-12-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_dish_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]
