# Generated by Django 3.2.12 on 2022-03-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
