# Generated by Django 4.0.3 on 2022-04-16 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0036_alter_choice_answered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='answered',
        ),
    ]
