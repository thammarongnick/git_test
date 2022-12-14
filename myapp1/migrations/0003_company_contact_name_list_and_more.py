# Generated by Django 4.1.1 on 2022-11-16 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_waste_item_master_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_contact_name_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.CharField(max_length=7, unique=True)),
                ('contact_name', models.CharField(default='', max_length=100)),
                ('contact_email', models.CharField(default='', max_length=100)),
                ('contact_phone', models.CharField(default='', max_length=10)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='waste_item_master_list',
            name='waste_unit',
            field=models.CharField(default='', max_length=5),
        ),
    ]
