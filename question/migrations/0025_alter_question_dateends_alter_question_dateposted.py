# Generated by Django 4.0.3 on 2022-04-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0024_alter_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dateEnds',
            field=models.DateTimeField(null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='datePosted',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
