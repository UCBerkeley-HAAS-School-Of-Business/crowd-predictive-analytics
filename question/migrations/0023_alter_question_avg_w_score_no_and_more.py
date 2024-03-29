# Generated by Django 4.0.3 on 2022-04-15 09:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0022_question_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='avg_w_score_no',
            field=models.FloatField(blank=True, null=True, verbose_name='avgN'),
        ),
        migrations.AlterField(
            model_name='question',
            name='avg_w_score_yes',
            field=models.FloatField(blank=True, null=True, verbose_name='avgY'),
        ),
        migrations.AlterField(
            model_name='question',
            name='equal_w_score_no',
            field=models.FloatField(blank=True, null=True, verbose_name='equalN'),
        ),
        migrations.AlterField(
            model_name='question',
            name='equal_w_score_yes',
            field=models.FloatField(blank=True, null=True, verbose_name='equalY'),
        ),
        migrations.AlterField(
            model_name='question',
            name='result',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='voters',
            field=models.ManyToManyField(blank=True, null=True, related_name='voters', to=settings.AUTH_USER_MODEL),
        ),
    ]
