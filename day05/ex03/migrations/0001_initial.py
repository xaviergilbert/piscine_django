# Generated by Django 3.0.5 on 2020-07-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('opening_crawl', models.TextField(null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
        ),
    ]