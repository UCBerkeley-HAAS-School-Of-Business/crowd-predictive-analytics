# Generated by Django 4.0.2 on 2022-03-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_question_novotes_question_yesvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='response',
            field=models.BooleanField(null=True),
        ),
    ]
