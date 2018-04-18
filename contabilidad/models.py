from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
#from phonenumber_field.modelsfield import PhoneNumberField

class Sector(models.Model):
  nombre=models.CharField(default="",max_length=20)
  def __str__(self):
    return self.nombre
  class Meta:
    verbose_name_plural="Sectores"

class Fecha(models.Model):
  fecha=models.DateField(default=date.today)
  def __str__(self):
    return str(self.fecha)
  class Meta:
    verbose_name_plural="Fechas"

class Proveedor(models.Model):
  nombre=models.CharField(default="",max_length=20)
  def __str__(self):
    return self.nombre
  class Meta:
    verbose_name_plural="Proveedores"

class Zona(models.Model):
  nombre=models.CharField(default="",max_length=20)
  def __str__(self):
    return self.nombre

class Ingreso(models.Model):
  fecha=models.ForeignKey(Fecha)
  monto=models.IntegerField(default=0)
  zona=models.ForeignKey(Zona)
  def __str__(self):
    return str(self.monto) + " " +str(self.fecha)

class Gasto(models.Model):
  fecha=models.ForeignKey(Fecha)
  obs=models.CharField(default="",max_length=30)
  def __str__(self):
    return str(self.fecha)+" "+str(self.monto)

class Concepto(models.Model):
  nombre=models.CharField(default="",max_length=30)
  sector=models.ForeignKey(Sector)
  def __str__(self):
    return self.nombre

class Detalle(models.Model):
  descripcion=models.CharField(default="",max_length=30)
  cant=models.DecimalField(max_digits=8,decimal_places=2,default=1)
  precio=models.DecimalField(decimal_places=2,max_digits=8)
  concepto=models.ForeignKey(Concepto)
  proveedor=models.ForeignKey(Proveedor)
  gasto=models.ForeignKey(Gasto)
  obs=models.CharField(default="",max_length=50)  
  def __str__(self):
    return str(self.cant)+ " " +self.descripcion

class Contacto(models.Model):
  nombre=models.CharField(default="",max_length=20)
  tel=models.IntegerField(default=0)
  empresa=models.ForeignKey(Proveedor)
  def __str__(self):
    return self.nombre
  class Meta:
    verbose_name_plural="Contactos"


