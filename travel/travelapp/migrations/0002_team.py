# Generated by Django 3.2.15 on 2022-09-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=250)),
                ('Timg', models.ImageField(upload_to='team')),
                ('desi', models.TextField()),
            ],
        ),
    ]
