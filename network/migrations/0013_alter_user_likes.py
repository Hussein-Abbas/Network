# Generated by Django 5.0.2 on 2024-04-30 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0012_alter_user_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="likes",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="liked_by",
                to="network.post",
            ),
        ),
    ]
