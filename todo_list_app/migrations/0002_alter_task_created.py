# Generated by Django 5.0.6 on 2024-07-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
