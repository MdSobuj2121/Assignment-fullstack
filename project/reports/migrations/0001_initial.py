# Generated by Django 5.1.1 on 2024-09-16 21:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('donation', 'Donation'), ('expense', 'Expense'), ('inventory', 'Inventory')], default='donation', max_length=20)),
                ('generated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='reports/')),
            ],
        ),
    ]
