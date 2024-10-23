# Generated by Django 5.1.2 on 2024-10-23 00:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')),  # menggunakan UUID sebagai primary key
                ('rating', models.PositiveIntegerField(validators=[models.MaxValueValidator(5), models.MinValueValidator(0)])),  # Rating dari 0 hingga 5
                ('review', models.TextField()),  # Menyimpan banyak kalimat
                ('date', models.DateTimeField(auto_now_add=True)),  # Tanggal pembuatan review
            ],
        ),
    ]
