from django.db import models

# Create your models here.
class Code(models.Model):
    code_nm = models.CharField(max_length=100) # 코드명
    comment = models.TextField(blank=True)  # 코드설명
    depth = models.IntegerField(blank=True) # 전체깊이
    sort = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.code_nm} ({self.id})"

    def code_id(self):
        return self.id

class CodeDt(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE, related_name="code")
    code_nm = models.CharField(max_length=100) # 코드명
    code_val = models.CharField(max_length=10) # 코드값
    comment = models.TextField(blank=True)  # 코드설명
    depth = models.IntegerField()
    sort = models.IntegerField()

    def __str__(self):
        return f"{self.code_nm}"

    def code_id(self):
        return self.id

# # upload_to : 업로드될 폴더명으로 media/user/2022에 쌓이게 된다
# pic = models.ImageField(upload_to="user/%y")

# def getpic(self):
#     if self.pic:
#         return self.pic.url
#     return "/media/noimage.png"