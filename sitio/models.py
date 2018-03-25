from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
class Galpon(models.Model):
  nombre=models.CharField(max_length=20)
  produccion=models.BooleanField(default=True)
  def __str__(self):
    return self.nombre
  class Meta:
    verbose_name_plural='Galpones'

class Color(models.Model):
  nombre=models.CharField(max_length=20)
  def __str__(self):
    return self.nombre
  class Meta:
    verbose_name_plural='Colores'

class Plantel(models.Model):
  nombre=models.CharField(max_length=20)
  color=models.ForeignKey(Color)
  es_activo=models.BooleanField(default=True)
  cantidad=models.IntegerField(default=0)
  nacimiento=models.DateField(default=date.today)
  galpon=models.ForeignKey(Galpon)
  def __str__(self):
    return self.nombre
  def proximo(self,):
    este=0
    galpones=Galpon.objects.all().order_by('id')
    for galpon in galpones:
      planteles=galpon.plantel_set.all().filter(es_activo=True).order_by('-nacimiento')
      for plantel in planteles:
        if este:
          return plantel
        if self==plantel:
          este=1
    return None
  class Meta:
    verbose_name_plural='Planteles'

class Fecha(models.Model):
  fecha=models.DateField(default=date.today)
  def __str__(self):
    return str(self.fecha)
  class Meta:
    verbose_name_plural='Fechas'

class Anotacion(models.Model):
  usuario=models.ForeignKey(User)
  fecha=models.ForeignKey(Fecha)
  hora=models.TimeField()
  plantel=models.ForeignKey(Plantel)
  muertes=models.IntegerField(default=0)
  postura=models.IntegerField(default=0)
  comentario=models.CharField(max_length=200,blank=True)  
  class Meta:
    verbose_name_plural='Anotaciones'
  def proximo(self,):
      este=0
      galpones=Galpon.objects.all().order_by('id').values_list('id')
      for galpon in galpones:
        planteles=Galpon.get(pk=galpon.id).plantel_set.all().filter(es_activo=True).order_by('-nacimiento').values_list('id')
        for plantel in planteles:
          if este:
            return Plantel.objects.get(pk=este)
          if self.id==plantel:
            este=1
      return None
      
      

#  def sumarAnteriores(self, ):
#    anterior=self.objects.all().filter('fecha.date)
