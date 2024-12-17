from django.db import models

# Create your models here.

class Modelo(models.Model):
    idclient=models.CharField("id",max_length=10,unique=True,default="")
    client=models.CharField("Client Name",max_length=40,default="")
    typescale=models.CharField("Scale Model", max_length=20,default="")
    capacity=models.CharField("Capacity Scale", max_length=30,default="")
    Collaborators=models.CharField("Collaborator",max_length=40,default="")

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural="Modelos"
