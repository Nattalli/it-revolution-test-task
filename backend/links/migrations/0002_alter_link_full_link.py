# Generated by Django 4.2.11 on 2024-03-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("links", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="full_link",
            field=models.TextField(unique=True),
        ),
    ]
