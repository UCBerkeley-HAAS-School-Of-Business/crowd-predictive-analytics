# Generated by Django 4.0.3 on 2022-04-15 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0019_remove_choice_question_choice_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='question.question'),
        ),
    ]
