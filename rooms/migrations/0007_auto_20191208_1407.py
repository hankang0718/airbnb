# Generated by Django 2.2.5 on 2019-12-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20191117_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='얼마나 많은 손님이 주무실거에요?'),
        ),
    ]
