from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    class Meta:
        app_label = 'bands'
    
    def __str__(self):
        return f"Musician(id={self.id}, last_name={self.last_name})"
