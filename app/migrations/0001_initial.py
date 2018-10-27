# Generated by Django 2.0.9 on 2018-10-27 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='banners')),
                ('titulo', models.CharField(blank=True, max_length=250, null=True)),
                ('subtitulo', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='registro_empresa')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validado', models.BooleanField(default=False)),
                ('nombreTitular', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('numeroTelefonotitular', models.CharField(blank=True, max_length=20, null=True)),
                ('direccionTitular', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(max_length=100)),
                ('nombreEmpresa', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('municipio', models.CharField(blank=True, max_length=50, null=True)),
                ('direccionEmpresa', models.CharField(blank=True, max_length=100, null=True)),
                ('numTel', models.CharField(blank=True, max_length=20, null=True)),
                ('quieninvito', models.CharField(blank=True, max_length=50, null=True)),
                ('loginmkt', models.CharField(blank=True, max_length=50, null=True)),
                ('porcentaje', models.IntegerField(blank=True, default=0, null=True)),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('youtube', models.URLField()),
                ('twitter', models.URLField()),
                ('whatsapp', models.URLField()),
                ('sitioweb', models.URLField()),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Categoria')),
                ('imagenes', models.ManyToManyField(to='app.Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=100)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pais')),
            ],
            options={
                'verbose_name': 'Ubicacion',
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
        migrations.AddField(
            model_name='negocio',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pais'),
        ),
        migrations.AddField(
            model_name='negocio',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
