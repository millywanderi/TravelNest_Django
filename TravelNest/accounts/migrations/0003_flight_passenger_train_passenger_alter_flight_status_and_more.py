# Generated by Django 4.2.5 on 2023-09-13 15:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0002_alter_flight_status_train"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="passenger",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="train",
            name="passenger",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="flight",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Cancelled", "CANCELLED"),
                    ("Delayed", "DELAYED"),
                    ("On Time", "ON_TIME"),
                ],
                max_length=9,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="train",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Cancelled", "CANCELLED"),
                    ("Delayed", "DELAYED"),
                    ("On Time", "ON_TIME"),
                ],
                max_length=9,
                null=True,
            ),
        ),
    ]