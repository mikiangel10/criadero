from django.contrib import admin
from django.contrib.auth.models import User
from .models import Anotacion,Plantel,Galpon,Fecha 

class AdminGalpon(admin.ModelAdmin):
  list_display=['nombre']
  def __str__(self):  
    return self.nombre  
class AdminAnotacion(admin.ModelAdmin):
  list_display=['plantel','postura','muertes','fecha']
  list_filter=['fecha','plantel']
  search_fields=['plantel']
  #date_hierarchy=('fecha')
class AdminFecha(admin.ModelAdmin):
  list_display=['fecha']
class AdminPlantel(admin.ModelAdmin):
  list_display=['nombre','color','cantidad','nacimiento']

admin.site.register(Anotacion,AdminAnotacion)
admin.site.register(Fecha,AdminFecha)
admin.site.register(Plantel,AdminPlantel)
admin.site.register(Galpon,AdminGalpon)


  
