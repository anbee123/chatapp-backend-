# Generated by Django 4.1 on 2023-02-20 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.CharField(default=None, max_length=100000),
            preserve_default=False,
        ),
    ]
