# Generated by Django 3.2 on 2021-04-08 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reserved_end_date', models.DateTimeField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Building'), (1, 'Requested'), (2, 'Accepted'), (3, 'Denied'), (4, 'Borrowed'), (5, 'Returned')], default=0)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('base_url', models.URLField(default='http://localhost:8000')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('amount_field', models.CharField(max_length=150)),
                ('borrowed', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.reservation')),
            ],
        ),
    ]
