from django.contrib import admin
from django.contrib.auth.models import User
from .models import Anotacion,Plantel,Galpon,Fecha,Color
<<<<<<< HEAD

=======
>>>>>>> 420b33389db626602ccd6d9e22e817292222c7a0
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
class AdminColor(admin.ModelAdmin):
<<<<<<< HEAD
  list_display=['nombre']
=======
	list_display=['nombre']

>>>>>>> 420b33389db626602ccd6d9e22e817292222c7a0
admin.site.register(Anotacion,AdminAnotacion)
admin.site.register(Fecha,AdminFecha)
admin.site.register(Plantel,AdminPlantel)
admin.site.register(Galpon,AdminGalpon)
admin.site.register(Color,AdminColor)

  
