# Generated by Django 2.2.3 on 2019-07-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_app', '0002_auto_20190707_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Scheduled', 'Scheduled'), ('Actual', 'Actual')], max_length=9),
        ),
    ]
