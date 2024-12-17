from django import forms
from .models import *

class ModeloForm(forms.ModelForm):
    class Meta:
        model=Modelo
        fields = "__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*argg,**kwargs)
        for field in iter(self.fields):
            self.field[field].widget.attrs.update({
                'class': 'form-control'
            })