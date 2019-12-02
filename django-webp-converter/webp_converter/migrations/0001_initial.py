# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WebPImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        serialize=False,
                        verbose_name="ID",
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("static_path", models.CharField(max_length=512)),
                ("quality", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="webpimage", unique_together=set([("static_path", "quality")]),
        ),
    ]
