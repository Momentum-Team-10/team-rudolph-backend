# Generated by Django 4.0 on 2021-12-21 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_merge_20211220_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('created_at',)},
        ),
        migrations.RemoveField(
            model_name='question',
            name='votes',
        ),
    ]
