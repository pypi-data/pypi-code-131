# Generated by Django 3.2.14 on 2022-08-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=80)),
                ('priority', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DemoTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.demoone')),
            ],
        ),
    ]
