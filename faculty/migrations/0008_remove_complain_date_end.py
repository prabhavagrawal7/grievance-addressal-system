# Generated by Django 4.0.4 on 2022-04-23 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0007_alter_complain_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='date_end',
        ),
    ]
