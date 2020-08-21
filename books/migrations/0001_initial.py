# Generated by Django 2.2.15 on 2020-08-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=250)),
                ('book_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('review', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
