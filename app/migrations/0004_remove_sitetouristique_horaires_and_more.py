# Generated by Django 5.0.1 on 2024-02-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_partenaire_sites_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitetouristique',
            name='horaires',
        ),
        migrations.RemoveField(
            model_name='sitetouristique',
            name='tarifs',
        ),
    ]
