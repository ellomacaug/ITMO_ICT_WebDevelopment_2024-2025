# Generated by Django 4.2.7 on 2023-11-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0002_registration_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
