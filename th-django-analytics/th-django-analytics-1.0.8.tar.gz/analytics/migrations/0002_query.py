# Generated by Django 4.0.5 on 2022-08-11 01:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Query",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        help_text="Nome do parâmetro que sera adicionado no contexto com o resultado desta query",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "query",
                    models.TextField(
                        blank=True,
                        default="\n{% set body = {} %}\n{{body}}\n",
                        null=True,
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "position",
                    models.PositiveSmallIntegerField(
                        help_text="Posição de processamento",
                        null=True,
                        verbose_name="Position",
                    ),
                ),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "dashboard",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dashboardQuery",
                        to="analytics.dashboard",
                        verbose_name="dashboard",
                    ),
                ),
            ],
            options={
                "verbose_name": "Query",
                "verbose_name_plural": "Querys",
                "ordering": ["position"],
            },
        ),
    ]
