# Generated by Django 3.0.7 on 2021-07-19 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mark1', '0012_login_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='userid',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]