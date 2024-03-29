# Generated by Django 4.0.3 on 2022-04-10 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0012_alter_question_result_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No'), (None, 'None')], default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='result',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='question.results'),
        ),
    ]
