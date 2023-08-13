# Generated by Django 4.2.4 on 2023-08-13 10:21

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(choices=[('Delux', 'Delux'), ('Luxury', 'Luxury'), ('Luxury Suite', 'Luxury Suite'), ('Presidental Suite', 'Presidental Suite')], max_length=20)),
                ('room_no', models.CharField(max_length=10, unique=True)),
                ('room_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UnavailableRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unavailable_dates', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=None)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guest_name', models.CharField(max_length=50)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rooms')),
            ],
        ),
    ]
