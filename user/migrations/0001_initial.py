# Generated by Django 3.2.6 on 2021-08-14 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
