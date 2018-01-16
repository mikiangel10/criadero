from django.conf.urls import  url

from . import views

urlpatterns=[
  url(r'^$',views.inicio,name='inicio'),
  url(r'^planteles/$',views.planteles,name='planteles'),
  url(r'^registros/$',views.registros,name='registros'),
  url(r'^postura/$',views.anotacion,name='anotacion'),
  url(r'^postura/anotar/(?P<plantel_id>[0-9]+)$',views.nueva_anotacion,name='nueva_anotacion'),  
  url(r'^copiar/$',views.actualizar_desde_archivo),


]
