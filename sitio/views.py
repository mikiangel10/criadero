from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import AnotacionForm#,myAnotacionForm
from django.forms import formset_factory
from sitio.models import Plantel, Galpon,Color,Anotacion,Fecha
import datetime

def inicio(request):
	return render(request, 'sitio/inicio.html',{})

def planteles(request):
  nombres=Plantel.objects.all()
  return render(request, 'sitio/planteles.html',{'planteles':nombres})

def registros(request):
  dia=datetime.timedelta(1)
  galpones_reg=Galpon.objects.all()
  planteles=Plantel.objects.all().filter(es_activo=True)
  registros=Anotacion.objects.all()
  galpones={}
  for galpon in galpones_reg:
    planteles_lista=[]
    for plantel in planteles:
      if plantel.galpon==galpon:
        planteles_lista.append(plantel)
    galpones[galpon]=planteles_lista

  fechas=Fecha.objects.order_by('fecha')
  posturas={}
  for fecha in fechas:
    dics={}
    for plantel in planteles:
      postura=0
      for reg in registros.filter(plantel=plantel).filter(fecha=fecha):
        postura=postura+reg.postura
      dics[plantel]=postura
    posturas[fecha]=dics
 
  return render(request,'sitio/registros.html',{'posturas':posturas,'galpones':galpones,})

def nueva_anotacion(request,plantel_id):
  hoy=datetime.date.today()
  usuario=request.user
  p=Plantel.objects.get(pk=plantel_id)
  if request.method=='POST':
    form=AnotacionForm(request.POST)
    if form.is_valid():
      hoy=Fecha.objects.get_or_create(fecha=hoy)[0]
      anotado=Anotacion.objects.filter(fecha=hoy.id, plantel=p)
      com=form.cleaned_data['comentario']
      post=form.cleaned_data['postura']
      muer=form.cleaned_data['muertes']
      hora=datetime.datetime.now().time()
      if anotado:
        anotado=anotado.first()         
        anotado.postura+=post
        anotado.muertes+=muer
        anotado.comentario+=com
        anotado.hora=hora
        anotado.save()

      else:
        anotado=Anotacion.objects.create(plantel=p,usuario=usuario, fecha=hoy,comentario=com,muertes=muer,postura=post,hora=hora)
    #  raise()
      return HttpResponseRedirect('/postura/')
    else:
      return render(request,'sitio/anotacion1.html',{'form':form})
  else:
    form=AnotacionForm()
    return render(request,'sitio/anotacion1.html',{'form':form})

def anotacion(request):
  hoy=Fecha.objects.get_or_create(fecha=datetime.date.today())[0]
  planteles=Plantel.objects.filter(es_activo=True)
  registros=hoy.anotacion_set.all()
  regs={}
  for galpon in Galpon.objects.filter(produccion=True):
    reg_plantel={}
    for plantel in planteles.filter(galpon=galpon):
      postura=0
      muertes=0
      anotadas=registros.filter(plantel=plantel)
      if anotadas.count()==0:
        registro={postura:0,muertes:0}
      else:
        for registro in anotadas:
          postura+=registro.postura
          muertes+=registro.muertes
      reg_plantel[plantel]=(postura,muertes,registro)
    regs[galpon]=reg_plantel

  #regs={galpon:{plantel=(postura,muertes,form),...},...}
    
  else:
    return render(request,'sitio/anotacion.html',{'registros':regs,})
  


def actualizar_desde_archivo(request):
  archivo=open("postura.txt","r")
  registros={}
  for linea in archivo:
    partes=linea.split('-')
    dia,mes,ano=partes[0].split('/')
    hora,minuto=partes[1].split(':')
    fecha=datetime.datetime(int(ano),int(mes),int(dia),int(hora),int(minuto))
    if 'Blancas_jovenes2' in partes[2]:   
      plantel=Plantel.objects.all().get(pk=1)
#completar la estructura con los pk segun la base de datos segun el nombre en postura.txt



    if registros.get(fecha):
      if registros[fecha].get(plantel):
        if 'muerte' in partes[2]:
          registros[fecha][plantel][1]+=int(partes[3])
        else:
          registros[fecha][plantel][0]+=int(partes[3]) 
      else:
        if 'muerte' in partes[2]:
          registros[fecha][plantel][1]+=int(partes[3])
        else:
          registros[fecha][plantel][0]+=int(partes[3])   
    else:
      registros[fecha][plantel]=[0,0]
      if 'muerte' in partes[2]:
        registros[fecha][plantel][1]+=int(partes[3])
      else:
        registros[fecha][0]+=int(partes[3])      
  return render(request,'sitio/copiados.html',{'registros':registros})
    

  
  
