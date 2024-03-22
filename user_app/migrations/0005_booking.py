# Generated by Django 5.0.3 on 2024-03-21 23:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('BookingExpert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_bookings', to=settings.AUTH_USER_MODEL)),
                ('CustomerUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
