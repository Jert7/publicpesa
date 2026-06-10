
from django.db import models

class County(models.Model):
    name = models.CharField(max_length=100)
    budget_allocated =models.DecimalField(max_digits=15, decimal_places=2)
    amount_spent =models.DecimalField(max_digits=15, decimal_places=2)
    projects_count =models.IntegerField(default=0)
    def __str__(self):
        return self.name 
    def percentage_spent(self):
         if self.budget_allocated ==0:
            return 0
         return (self.amount_spent / self.budget_allocated)*100
    


# Create your models here.
