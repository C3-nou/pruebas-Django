# Generated by Django 3.0.3 on 2020-02-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20200220_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, to='mascota.Vacunas'),
        ),
    ]