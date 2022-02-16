from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from common.models import CodeDt

# Create your views here.
## 로그인 ##
def login_user(request):
    if request.method == 'POST':
        iUsername = request.POST.get('username')
        iPassword = request.POST.get('password')

        user = authenticate(username=iUsername, password=iPassword)
        print(user)

        if user:
            login(request, user)
        
        # context={
        #     'staff_type': User.objects.get(username=iUsername)
        # }
        return render(request, 'acc/login.html')
        
    return render(request, 'acc/login.html')

## 로그아웃 ##
def logout_user(request):
    logout(request)
    return redirect('acc:login')

## 직원 등록 ##
# def join(request):
#     if request.method == 'POST':
#         # User.objects.create_user : 계정 생성
#         # 일반적인 객체 생성 후 save 시에는 오류는 없으나 패스워드가 평문 (비암호화)되어 추가된다
#         User.objects.create_user(
#             corpNbr = request.POST.get('corpNbr'),
#             staffTpCd = request.POST.get('staffTpCd'),
#             licensePlateNbr = request.POST.get('licensePlateNbr'),

#             username = request.POST.get('username'),
#             password = request.POST.get('password'),

#             last_name = request.POST.get('last_name'),
#             first_name = request.POST.get('first_name'),
#             telephone = request.POST.get('telephone'),
#             phoneNbr = request.POST.get('phoneNbr'),
#             email = request.POST.get('email'),
            
#             address = request.POST.get('address'),
#             address2 = request.POST.get('address2'),

#             bank = request.POST.get('bank'),
#             account = request.POST.get('account'),
#             comment = request.POST.get('comment'),
#         )

#         # request 에 레코드 입력 : 세션
#         # login(request, User.objects.get(username=iUsername))
#         return redirect('acc:login')

#     return render(request, 'acc/join.html')

# ## 직원목록조회 ##
# def staff(request):
#     context = {
#         'staffTypeCd' : CodeDt.objects.filter(codeId=1).exclude(cdVal='99'),
#         'staffList' : User.objects.exclude(staffTpCd='99')
#     }
#     return render(request, 'acc/staff.html', context)
