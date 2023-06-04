# Generated by Django 3.2 on 2023-06-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('author_name', models.CharField(max_length=300)),
            ],
        ),
    ]
