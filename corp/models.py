from django.db import models

# Create your models here.
class Corp(models.Model):
    corp_no = models.CharField(max_length=10)   #사업자번호 ○○○-○○-○○○○○
    corp_nm = models.CharField(max_length=50)   #회사명
    ceo = models.CharField(max_length=10)       #대표명
    zipcode = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=11, blank=True)
    cellphone = models.CharField(max_length=11, blank=True)
    bank = models.CharField(max_length=20, blank=True)
    account = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.corp_nm}"

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
