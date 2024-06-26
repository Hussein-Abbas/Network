# Generated by Django 5.0.2 on 2024-04-19 06:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0006_alter_user_followers_count_alter_user_following_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="followers_count",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="following_count",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
    ]
