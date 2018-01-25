# Generated by Django 2.0 on 2018-01-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0007_auto_20180108_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapath',
            old_name='datapath',
            new_name='host_name',
        ),
        migrations.RemoveField(
            model_name='datapath',
            name='object_datapath',
        ),
        migrations.AddField(
            model_name='datapath',
            name='ip_addres',
            field=models.TextField(null=True),
        ),
    ]
