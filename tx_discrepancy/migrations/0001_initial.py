# Generated by Django 3.0.3 on 2020-02-14 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Discrepancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('site_class', models.CharField(max_length=10)),
                ('report_status', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('sites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tx_discrepancy.Site')),
            ],
        ),
    ]
