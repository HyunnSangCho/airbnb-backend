# Generated by Django 4.1.5 on 2023-01-25 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Experiences",
            new_name="Experience",
        ),
    ]
