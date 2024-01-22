# Generated by Django 5.0.1 on 2024-01-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_available', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]