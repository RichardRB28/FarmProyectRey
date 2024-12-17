from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.

# VISTA GENERAL PARA SITIO DE MANTENIMIENTO DE BASCULAS

class HomeBascosta(generic.ListView):# nombre de la vista, hereda ListView
    permission_required= "app.view_modelo" #ubicacion del modelo
    model= Modelo # modelo de la vista
    template_name= "app/homeBascostaTemp.html"
    context_objetc_name= "obj"

# VISTA PARA LISTAR, BORRAR UN REGISTRO O EDITAR DE BASCULAS EN MANTENIMIENTO

class ModeloView(generic.ListView):# nombre de la vista, hereda ListView
    permission_required= "app.view_modelo" #ubicacion del modelo
    model= Modelo # modelo de la vista
    template_name= "modelo_list.html"
    context_objetc_name= "obj"

class ModeloNew(generic.CreateView):
    permission_required="app.add_modelo"
    model=Modelo
    template_name="app/modelo_form.html"
    context_objetc_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("app:modelo_list")

class ModeloEdit(generic.UpdateView):
    permission_required="app.change_modelo"
    model=Modelo
    template_name="app/modelo_form.html"
    context_objetc_name="obj"
    form_class=ModeloForm
    success_url=reverse_lazy("app:modelo_list")
    success_message="Modelo Actualizado Satisfactoriamente"
    
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)

class ModelDel(generic.DeleteView):
    permission_required="app.delete_modelo"
    model=Modelo
    template_name='app/catalogos_del.html'

