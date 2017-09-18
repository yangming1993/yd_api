# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Order(models.Model):
	orderId = models.CharField(max_length=20, primary_key=True)
	phone = models.CharField(max_length=11)
	itemId = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	price = models.CharField(max_length=10)
	quantity = models.CharField(max_length=1)
	finalFee = models.CharField(max_length=10)
	# discount = models.CharField(max_length=100)
	vcode = models.CharField(max_length=200)
	vcodePass = models.CharField(max_length=200)

