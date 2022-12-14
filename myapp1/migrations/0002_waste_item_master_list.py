# Generated by Django 4.1.1 on 2022-11-10 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waste_item_master_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_item_code', models.CharField(max_length=9, unique=True)),
                ('description_EN', models.CharField(default='', max_length=50)),
                ('description_TH', models.CharField(default='', max_length=100)),
                ('waste_group_code', models.CharField(default='', max_length=5)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
