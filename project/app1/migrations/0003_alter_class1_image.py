# Generated by Django 4.0.6 on 2022-07-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_class1_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class1',
            name='image',
            field=models.ImageField(upload_to='pics/justin'),
        ),
    ]
