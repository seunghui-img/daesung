from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Client
from common.models import Code,CodeDt

# Create your views here.
def list(request):
    # 거래처유형 콤보
    clienttypeQ = Q()
    clienttypeQ |= Q(id=5)
    clienttypeQ |= Q(id=6)
    clienttypeCombo = CodeDt.objects.filter(clienttypeQ)

    # 거래유형 콤보
    biztypeQ = Q()
    biztypeQ |= Q(id=7)
    biztypeQ |= Q(id=8)
    biztypeQ |= Q(id=9)
    biztypeCombo = CodeDt.objects.filter(biztypeQ)

    # 조회
    clienttype = request.GET.get('clienttype')
    biztype = request.GET.get('biztype')
    custnm = request.GET.get('custnm', '')

    print("GET : ", clienttype, biztype, custnm)

    searchQ = Q()

    # 거래처유형
    if clienttype:
        searchQ &= Q(client_type=clienttype)
        clienttype = int(clienttype)

    # 거래유형
    if biztype:
        searchQ &= Q(biz_type=biztype)
        biztype = int(biztype)
    
    # 거래처명
    if custnm:
        searchQ &= Q(cust_nm__contains=custnm)

    print("QuerySet : ", searchQ.__str__)

    list = Client.objects.filter(searchQ)

    print("Result : ", list)

    context={
        'clienttype_combo': clienttypeCombo,
        'biztype_combo': biztypeCombo,
        'clientlist': list,
        'search' : {
            'clienttype': clienttype,
            'biztype': biztype,
            'custnm': custnm,
        },
    }
    return render(request, 'client/list.html', context)

def create(request):
    return render(request, 'client/list.html')

def modify(request, pk):
    if request.method == 'POST':
        client = Client.objects.get(id=pk)

        client.client_type = CodeDt.objects.get(id=request.POST.get('client_type'))
        client.corp_no = request.POST.get('corp_no')
        client.corp_nm = request.POST.get('corp_nm')
        client.cust_nm = request.POST.get('cust_nm')
        client.biz_type = CodeDt.objects.get(id=request.POST.get('biz_type'))
        client.address = request.POST.get('address')
        client.address2 = request.POST.get('address2')
        client.telephone = request.POST.get('telephone')
        client.cellphone = request.POST.get('cellphone')
        client.bank = request.POST.get('bank')
        client.account = request.POST.get('account')
        client.save()
    return redirect('client:list')
    
def popup(request):
    print(request)
    m_clientnm = request.GET.get('m_clientnm')
    print('popup', m_clientnm)

    if m_clientnm:
        clientlist = Client.objects.filter(cust_nm__contains=m_clientnm)
    else:
        clientlist = Client.objects.all()

    context={
        'clientpoplist': clientlist,
        'm_clientnm': m_clientnm,
    }

    # return JsonResponse(context)
    return render(request, 'client/popup.html', context)