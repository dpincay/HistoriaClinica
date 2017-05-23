# Create your models here.

from __future__ import unicode_literals
from django.db import models


class Grupo_Cultural(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)


class Instruccion_Educativa(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)


class Pais(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)

    def __unicode__(self):
        return self.nombre

class Provincia(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

class Ciudad(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre


class Afinidad(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)

    def __unicode__(self):
        return self.nombre

class Pariente(models.Model):
    codigo = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, null=False)
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=40)
    afinidad = models.ForeignKey(Afinidad, on_delete=models.CASCADE)


class Paciente(models.Model):
    codigo = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, unique=True, null=False)
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=40)
    sexo = models.CharField(max_length=1, choices=(('m', 'Masculino'), ('f', 'Femenino')))
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    grupo_cultural = models.ForeignKey(Grupo_Cultural, on_delete=models.CASCADE)
    instruccion_educativa = models.ForeignKey(Instruccion_Educativa, on_delete=models.CASCADE)
    parientes = models.ManyToManyField(Pariente)


class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, unique=True, null=False)
    nombres = models.CharField(max_length=40, null=False)
    apellidos = models.CharField(max_length=40, null=False)
    login = models.CharField(max_length=30, unique=True, null=False)
    password = models.CharField(max_length=30, null=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=1, choices=(('a', 'Agendador'), ('m', 'Medico'), ('s', 'Administrador')))


class Agendador(models.Model):
    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Especialidad(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True, null=False)


class Medico(models.Model):
    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)


class Consultorio(models.Model):
    codigo = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=3, unique=True, null=False)
    nombre = models.CharField(max_length=30, unique=True, null=False)


class Enfermedad(models.Model):
    codigo = models.AutoField(primary_key=True)
    cie10 = models.CharField(max_length=5, unique=True, null=False)
    nombre = models.CharField(max_length=30, unique=True, null=False)


class Diagnostico(models.Model):
    codigo = models.AutoField(primary_key=True)
    enfermedad = models.ForeignKey(Enfermedad)
    tipo = models.CharField(max_length=3)


class Turno(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    observacion = models.CharField(max_length=100)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)


class Historia_Clinica(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    diagnosticos = models.ManyToManyField(Diagnostico)
    resumen_clinico = models.CharField(max_length=100)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)