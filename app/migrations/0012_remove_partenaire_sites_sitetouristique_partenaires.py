# Generated by Django 5.0.1 on 2024-02-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_partenaire_sites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partenaire',
            name='sites',
        ),
        migrations.AddField(
            model_name='sitetouristique',
            name='partenaires',
            field=models.ManyToManyField(blank=True, related_name='sites', to='app.partenaire'),
        ),
    ]
