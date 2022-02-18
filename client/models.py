from os import truncate
from django.db import models
from common.models import CodeDt

# Create your models here.
class Client(models.Model):
    client_type = models.ForeignKey(CodeDt, on_delete=models.PROTECT, null=True, related_name='client_client_type') #거래처유형코드 (P:개인,C:사업자)
    corp_no = models.CharField(max_length=10, null=True)   #사업자번호 ○○○-○○-○○○○○
    corp_nm = models.CharField(max_length=50, null=True)   #회사명
    
    cust_nm = models.CharField(max_length=50)    #고객명 또는 회사명

    biz_type = models.ForeignKey(CodeDt, on_delete=models.PROTECT, null=True, related_name='client_biz_type')    #거래유형코드 (S:판매, C:충전, R.임대)
    # mainBizPdtCd varchar  //주거래 상품
    
    zipcode = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=11, null=True)
    cellphone = models.CharField(max_length=11, null=True)
    bank = models.CharField(max_length=20, null=True)
    account = models.CharField(max_length=20, null=True)
    
    # stsCd varchar [default:'normal']    //거래상태 (정상, 거래중지)
    # comment varchar   //중지사유
    
    def __str__(self):
        return f"{self.cust_nm}"

    def fmt_corp_no(self):
        # ○○○-○○-○○○○○
        return f"{self.corp_no[:3]}-{self.corp_no[3:5]}-{self.corp_no[5:10]}"

    def fmt_telephone(self):
        nbr1 = nbr2 = nbr3 = ''

        if len(self.telephone) == 11:
            # ○○○-○○○○-○○○○
            nbr1 = self.telephone[:3]
            nbr2 = self.telephone[3:7]
            nbr3 = self.telephone[7:11]
        elif len(self.telephone) == 10:
            if self.telephone[:2] == '02':
                # ○○-○○○○-○○○○
                nbr1 = self.telephone[:2]
                nbr2 = self.telephone[2:6]
                nbr3 = self.telephone[6:10]
            else:
                # ○○○-○○○-○○○○
                nbr1 = self.telephone[:3]
                nbr2 = self.telephone[3:6]
                nbr3 = self.telephone[6:10]
        else:
            return self.telephone

        return f"{nbr1}-{nbr2}-{nbr3}"

    def fmt_cellphone(self):
        # ○○○-○○○○-○○○○
        return f"{self.cellphone[:3]}-{self.cellphone[3:7]}-{self.cellphone[7:11]}"
