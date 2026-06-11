from django.db import models

class County(models.Model):
    name = models.CharField(max_length=100)
    budget_allocated = models.DecimalField(max_digits=15, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=15, decimal_places=2)
    projects_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def percentage_spent(self):
        if self.budget_allocated == 0:
            return 0
        return (self.amount_spent / self.budget_allocated) * 100


class Tender(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='tenders')
    name = models.CharField(max_length=200)
    company_awarded = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_awarded = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.name} - {self.county.name}"


class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('stalled', 'Stalled'),
        ('completed', 'Completed'),
    ]
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')

    def __str__(self):
        return f"{self.name} - {self.county.name}"
    