# Generated by Django 4.0 on 2021-12-20 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_answer_answers_votes_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('votes', 'created_at')},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('votes', 'created_at')},
        ),
        migrations.RemoveConstraint(
            model_name='answer',
            name='answers_votes_date',
        ),
        migrations.RemoveConstraint(
            model_name='question',
            name='questions_votes_date',
        ),
    ]
