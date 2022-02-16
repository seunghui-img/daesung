from django.db import models
from client.models import Client
from acc.models import User
from product.models import Product
from common.models import CodeDt

# Create your models here.
class Order(models.Model):
    order_no = models.CharField(max_length=11)  #거래번호 yyyymmdd-ooo
    orderdate = models.CharField(max_length=8)  #거래일자 yyyymmdd
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="order_client")       #거래처
    staff = models.ForeignKey(User, on_delete=models.PROTECT, related_name="order_staff")           #담당직원
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="order_product")    #거래상품
    biz_type = models.ForeignKey(CodeDt, on_delete=models.PROTECT, related_name="order_biz_type")   #거래유형코드 (S:판매, C:충전, R.임대)
    unit = models.CharField(max_length=50)      #단위
    unit_price = models.IntegerField()          #단가
    quantity = models.IntegerField(default=1)   #수량
    ammount = models.IntegerField()             #총 금액
    
    approver = models.CharField(max_length=50)  #결제인
    payment_type = models.ForeignKey(CodeDt, on_delete=models.PROTECT, related_name="order_payment_type")     #결제유형코드 (1:현금, 2:카드, 3:이체)
    payment_state = models.ForeignKey(CodeDt, on_delete=models.PROTECT, related_name="order_payment_state")   #결제상태코드 (1:미납, 0:완료)
    
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.order_no}"
