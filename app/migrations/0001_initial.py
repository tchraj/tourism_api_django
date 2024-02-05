# Generated by Django 5.0.1 on 2024-02-05 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_partenaire', models.CharField(max_length=60)),
                ('localisation', models.CharField(max_length=120)),
                ('type_partenaire', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_region', models.CharField(max_length=30)),
                ('nombre_sites', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SiteTouristique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_site', models.CharField(max_length=100)),
                ('nombre_partenaires', models.IntegerField()),
                ('localisation', models.CharField(max_length=120)),
                ('services', models.TextField()),
                ('description', models.TextField()),
                ('horaires', models.JSONField(default=dict)),
                ('tarifs', models.JSONField(default=dict)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region')),
            ],
        ),
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.partenaire')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sitetouristique')),
            ],
        ),
        migrations.CreateModel(
            name='Touriste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_touriste', models.CharField(max_length=60)),
                ('prenoms_touriste', models.CharField(max_length=60)),
                ('tel', models.CharField(max_length=15)),
                ('partenaires', models.ManyToManyField(to='app.partenaire')),
                ('sites', models.ManyToManyField(to='app.sitetouristique')),
            ],
        ),
    ]
