# Generated by Django 3.2.14 on 2022-08-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psu_export', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportfield',
            name='key',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
