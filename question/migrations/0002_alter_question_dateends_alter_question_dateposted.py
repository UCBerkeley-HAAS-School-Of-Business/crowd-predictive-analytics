# Generated by Django 4.0.3 on 2022-03-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dateEnds',
            field=models.DateTimeField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='datePosted',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]