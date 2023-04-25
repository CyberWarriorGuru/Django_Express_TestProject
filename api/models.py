from django.db import models

# Create your models here.
class DataCSV(models.Model):
    username = models.CharField(max_length=200)
    csv_filepath = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.csv_filepath