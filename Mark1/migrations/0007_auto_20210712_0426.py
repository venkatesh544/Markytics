# Generated by Django 3.0.7 on 2021-07-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mark1', '0006_sent_slt2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sent',
            name='message2',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sent',
            name='message3',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
