# Generated by Django 4.0.3 on 2022-04-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0026_remove_question_voters_question_voters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ManyToManyField(blank=True, default=1, null=True, to='question.category'),
        ),
    ]
