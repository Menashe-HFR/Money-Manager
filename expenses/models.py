from django.db import models

# Create your models here.


class ExpenseCategory(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(auto_now_add=True)
