from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CodeDt
from corp.models import Corp

# Create your models here.
class User(AbstractUser):

    staff_type = models.ForeignKey(CodeDt, on_delete=models.PROTECT, null=True, related_name='user_staff_type')    #직원유형코드 (99매니저, 1벌크, 2용기, 3경리)
    corp = models.ForeignKey(Corp, on_delete=models.PROTECT, null=True, related_name='user_corp') #소속회사

    birthday = models.CharField(max_length=10, blank=True)#yyyy-mm-dd
    zipcode = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=11, blank=True)
    cellphone = models.CharField(max_length=11, blank=True)
    bank = models.CharField(max_length=20, blank=True)
    account = models.CharField(max_length=20, blank=True)
    date_retired = models.CharField(max_length=10, blank=True)   # 퇴사일
    comment = models.TextField(blank=True)
    license_plate_number = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return f"{self.username}"

    def fmt_cellphone(self):
        # ○○○-○○○○-○○○○
        if self.cellphone and len(self.cellphone) == 11:
            return f"{self.cellphone[:3]}-{self.cellphone[3:7]}-{self.cellphone[7:11]}"
        else:
            return self.cellphone

    def staff_type_val(self):
        return self.staff_type.code_val
        
    def id(self):
        return self.id