# Generated by Django 4.0 on 2021-12-14 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='answered',
        ),
    ]
