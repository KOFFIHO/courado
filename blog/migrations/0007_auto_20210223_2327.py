# Generated by Django 3.1 on 2021-02-23 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_defile_telerphone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defile',
            old_name='telerphone',
            new_name='telephone',
        ),
    ]
