from django.db import models

# Create your models here.


class Product(models.Model):
	code = models.CharField(max_length=25, unique=True)
	name = models.CharField(max_length=150)
	quantity = models.PositiveIntegerField()
	create = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(null=True)



