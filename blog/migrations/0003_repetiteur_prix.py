# Generated by Django 3.1 on 2021-01-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210115_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='repetiteur',
            name='prix',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
