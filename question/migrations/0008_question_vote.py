# Generated by Django 4.0.2 on 2022-04-10 00:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0007_alter_choice_options_choice_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='vote',
            field=models.ManyToManyField(blank=True, default=None, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
