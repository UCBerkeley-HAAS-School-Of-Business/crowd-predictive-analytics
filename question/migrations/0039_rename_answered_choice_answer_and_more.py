# Generated by Django 4.0.3 on 2022-04-19 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0038_choice_answered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='answered',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='response',
            new_name='user_responded',
        ),
    ]