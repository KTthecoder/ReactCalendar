# Generated by Django 3.2.8 on 2022-11-24 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitiesmodel',
            name='status',
            field=models.CharField(choices=[('Important', 'Important'), ('Long Term', 'Long Term'), ('Short Term', 'Short Term')], default='Short Term', max_length=20),
        ),
        migrations.AddField(
            model_name='subactivitesmodel',
            name='status',
            field=models.CharField(choices=[('Important', 'Important'), ('Long Term', 'Long Term'), ('Short Term', 'Short Term')], default='Short Term', max_length=20),
        ),
        migrations.AlterField(
            model_name='activitiesmodel',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subactivitesmodel',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subActivity', to='calendarApp.activitiesmodel'),
        ),
        migrations.AlterField(
            model_name='subactivitesmodel',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
