from django import forms
import datetime

from .models import Anotacion,Plantel,Fecha

class AnotacionForm(forms.ModelForm):

  class Meta:
        model = Anotacion
        fields = ('postura', 'muertes','comentario')

#class myAnotacionForm(AnotacionForm):
#  def __init__(self,*args,user,plantel,**kwargs):
#    self.user=user
#    
#    self.pantel=plantel

