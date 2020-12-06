from django.db import models

# Create your models here.
class Data(models.Model):
	created_by = models.CharField(max_length=90)
	generated_for = models.CharField(max_length=100)
	coupon_no = models.AutoField()
	amount = models.CharField(max_length=100)

	def __repr__(self):
		return (f"Coupon for {self.generated_for}")

	def __str__(self):
		return (f"Coupon for {self.generated_for}")
