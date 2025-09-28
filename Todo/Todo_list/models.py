from django.db import models
from datetime import date
# Create your models here.

class Todo(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length= 200, default= "New Todo")
    done = models.BooleanField(default=False)

    def __str__(self):
        return "Id: " + str(self.id) + "    Name: " + self.name