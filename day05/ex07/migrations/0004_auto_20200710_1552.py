# Generated by Django 3.0.5 on 2020-07-10 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0003_auto_20200710_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
