# Generated by Django 5.0 on 2024-05-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('booking_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
