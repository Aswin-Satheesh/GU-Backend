# Generated by Django 5.1.4 on 2025-04-22 16:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetails",
            fields=[
                ("User_ID", models.AutoField(primary_key=True, serialize=False)),
                ("First_Name", models.CharField(max_length=100)),
                ("Last_Name", models.CharField(max_length=100)),
                ("Email_Address", models.EmailField(max_length=254, unique=True)),
                ("Phone_Number", models.CharField(max_length=15, unique=True)),
                ("Password", models.CharField(max_length=128)),
                ("is_active", models.BooleanField(default=True)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("Created_At", models.DateTimeField(default=django.utils.timezone.now)),
                ("Updated_At", models.DateTimeField(auto_now=True)),
                ("pincode", models.CharField(max_length=10)),
                ("address", models.TextField()),
                ("DOB", models.DateTimeField(blank=True, null=True)),
                ("Gender", models.CharField(max_length=50)),
                ("Proof", models.CharField(max_length=100)),
                ("Expertise", models.TextField()),
                ("Years_of_Experience", models.IntegerField(default=0)),
                ("organization_detail", models.CharField(max_length=200)),
                ("Field_of_Interest", models.TextField()),
                ("Requirements", models.TextField()),
            ],
        ),
    ]
