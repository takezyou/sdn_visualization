# Generated by Django 2.0 on 2017-12-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0005_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='updated',
            field=models.IntegerField(null=True),
        ),
    ]
