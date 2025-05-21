from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    type_choices=[
            ('Income','Income',),
            ('Expense', 'Expense')]

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=30)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField()
    description=models.TextField(blank=True)
    type=models.CharField(max_length=20, choices=type_choices)

    def _str__(self):
        return self.title
    
