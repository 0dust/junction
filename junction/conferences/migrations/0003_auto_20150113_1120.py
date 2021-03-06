# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0002_auto_20150109_1527"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="conference",
            options={
                "get_latest_by": "start_date",
                "verbose_name": "Conference",
                "ordering": ("-start_date", "name"),
                "verbose_name_plural": "Conferences",
            },
        ),
    ]
