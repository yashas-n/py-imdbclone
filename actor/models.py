from django.db import models

# Create your models here.
 
class Actor(models.Model):  
    edob = models.CharField(max_length=8)  
    ename = models.CharField(max_length=100)  
    esex = models.CharField(max_length=6)  
    ebio = models.CharField(max_length=600)  
    class Meta:  
        db_table = "actor"  
