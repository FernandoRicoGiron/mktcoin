# Generated by Django 2.0.9 on 2018-10-26 05:14

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181026_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacion',
            name='address',
            field=django_google_maps.fields.AddressField(default='', max_length=200),
            preserve_default=False,
        ),
    ]