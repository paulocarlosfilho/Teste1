# Generated by Django 5.1.6 on 2025-02-16 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("to_do", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="to_do",
            old_name="createde_at",
            new_name="created_at",
        ),
    ]
