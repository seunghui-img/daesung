from django.db import models
from common.models import CodeDt

# Create your models here.
class Product(models.Model):
    product_ctgy = models.ForeignKey(CodeDt, on_delete=models.SET_NULL, null=True, related_name='product_product_ctgy')   #상품분류코드 (1:압축가스, 2:액화가스, 3:용해가스)
    product_nm = models.CharField(max_length=50)    #상품명

    unit = models.CharField(max_length=50, blank=True)  #단위
    unit_price = models.IntegerField(default=0)         #단가

    comment = models.TextField(blank=True)

    def __str__(self):
        return self.product_nm