# Generated by Django 2.0.9 on 2018-10-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20181026_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='validado',
            field=models.BooleanField(default=False),
        ),
    ]