# Generated by Django 3.0.5 on 2020-07-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex07', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='update',
            field=models.DateField(auto_now_add=True),
        ),
    ]
