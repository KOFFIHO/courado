# Generated by Django 3.1 on 2021-01-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210116_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulaire',
            name='cv',
            field=models.FileField(blank=True, upload_to='stokRepetiteur'),
        ),
        migrations.AlterField(
            model_name='formulaire',
            name='phOto',
            field=models.ImageField(blank=True, upload_to='stokRepetiteur'),
        ),
        migrations.AlterField(
            model_name='formulaire',
            name='photopi',
            field=models.FileField(blank=True, upload_to='stokRepetiteur'),
        ),
    ]
