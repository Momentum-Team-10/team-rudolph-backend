# Generated by Django 4.0 on 2021-12-16 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_answer_voted_on_question_voted_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answered',
        ),
    ]