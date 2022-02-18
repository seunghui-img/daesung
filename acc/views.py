from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import User
from common.models import CodeDt

# Create your views here.
''' 인증 '''
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
        return redirect('order:sales-list')
        
    return render(request, 'acc/login.html')

def logout_user(request):
    logout(request)
    return redirect('acc:login')


''' 직원 관리 '''
def staff_list(request):
    #직원유형 콤보
    staff_typeQ = Q()
    staff_typeQ |= Q(id=1)
    staff_typeQ |= Q(id=2)
    staff_typeQ |= Q(id=3)
    
    context = {
        'stafftype_combo' : CodeDt.objects.filter(staff_typeQ),
        'stafflist' : User.objects.exclude(staff_type=0)
    }
    return render(request, 'acc/staff-list.html', context)

def modify_staff(request, staffid):
    if request.method == 'POST':
        staff = User.objects.get(id=staffid)
        
        staff.staff_type = CodeDt.objects.get(id=request.POST.get('staff_type'))

        from corp.models import Corp
        staff.corp = Corp.objects.get(id=1)

        staff.birthday = request.POST.get('birthday')
        staff.address = request.POST.get('address')
        staff.address2 = request.POST.get('address2')
        staff.telephone = request.POST.get('telephone')
        staff.cellphone = request.POST.get('cellphone')
        staff.bank = request.POST.get('bank')
        staff.account = request.POST.get('account')
        staff.date_retired = request.POST.get('date_retired', '')
        staff.comment = request.POST.get('comment')
        staff.license_plate_number = request.POST.get('license_plate_number')
        staff.save()

        return redirect('acc:staff')

# def create_staff(request):
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