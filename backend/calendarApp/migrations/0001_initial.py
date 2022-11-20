# Generated by Django 4.1.3 on 2022-11-20 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('finished', models.BooleanField(default=False)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubActivitesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('finished', models.BooleanField(default=False)),
                ('note', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarApp.activitiesmodel')),
            ],
        ),
    ]
