# --encoding: utf-8

from django import forms
from products import models as prod_models


class ProductForm(forms.ModelForm):

	class Meta:
		model = prod_models.Product
		fields = ('code', 'name', 'quantity')