# Generated by Django 4.0.3 on 2022-04-10 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0010_category_question_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='result',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='question.result'),
        ),
        migrations.AlterField(
            model_name='result',
            name='outcome',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No'), (None, 'None')], default=None),
        ),
    ]
