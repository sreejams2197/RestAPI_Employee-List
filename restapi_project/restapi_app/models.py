from django.db import models

# Create your models here.
class employees(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    EmpId = models.IntegerField()
    def __str__(self):
        return self.Name
