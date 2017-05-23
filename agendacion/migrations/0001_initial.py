# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afinidad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agendador',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('serie', models.CharField(max_length=3, unique=True)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('serie', models.CharField(max_length=3, unique=True)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_Cultural',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historia_Clinica',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('resumen_clinico', models.CharField(max_length=100)),
                ('diagnosticos', models.ManyToManyField(to='agendacion.Diagnostico')),
            ],
        ),
        migrations.CreateModel(
            name='Instruccion_Educativa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=40)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Ciudad')),
                ('grupo_cultural', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Grupo_Cultural')),
                ('instruccion_educativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Instruccion_Educativa')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pariente',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=40)),
                ('afinidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Afinidad')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('observacion', models.CharField(max_length=100)),
                ('consultorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Consultorio')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('login', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('tipo_usuario', models.CharField(choices=[('a', 'Agendador'), ('m', 'Medico')], max_length=1)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='parientes',
            field=models.ManyToManyField(to='agendacion.Pariente'),
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Usuario'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Medico'),
        ),
        migrations.AddField(
            model_name='historia_clinica',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Paciente'),
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='enfermedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Enfermedad'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Provincia'),
        ),
        migrations.AddField(
            model_name='agendador',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendacion.Usuario'),
        ),
    ]
