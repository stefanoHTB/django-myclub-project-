# Generated by Django 4.0.5 on 2022-06-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0003_alter_event_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='venue owner'),
        ),
    ]