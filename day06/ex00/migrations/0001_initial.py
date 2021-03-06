# Generated by Django 3.0.5 on 2020-07-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('auteur', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('downvote', models.ManyToManyField(to='ex00.Downvote')),
                ('upvote', models.ManyToManyField(to='ex00.Upvote')),
            ],
        ),
    ]
