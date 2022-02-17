from django.shortcuts import redirect, render
from .models import Order
from common.models import CodeDt
from client.models import Client
from acc.models import User
from product.models import Product
from django.db.models import Q
import datetime

# Create your views here.
''' 판매관리 '''
def sales_list(request):
    # 조건 검색
    fromdate = request.GET.get('fromdate', '')
    todate = request.GET.get('todate', '')
    staffname = request.GET.get('staffname', '')
    # custNm = request.GET.get('custNm')

    print("GET : ", fromdate, todate, staffname)

    searchQ = Q()

    # 거래유형 : 판매
    searchQ &= Q(biz_type=7)

    # 주문일자
    searchQ &= Q(orderdate__range=[fromdate, todate])

    # 담당직원
    if staffname :
        try:
            staff = User.objects.get(username=staffname)
            searchQ &= Q(staff=staff)
        except:
            pass

    print("QuerySet : ", searchQ.__str__)

    list = Order.objects.filter(searchQ)

    print("Result : ", list)

    context = {
        'staff_combo': User.objects.filter(is_staff=False).exclude(staff_type=4),
        'saleslist': list,
        'search' : {
            'staffname': staffname,
            'fromdate': fromdate,
            'todate': todate,
        },
    }

    return render(request, 'order/sales-list.html', context)

def create_sales(request):
    print(request.method, 'create_sales')

    if request.method == 'POST':
        insert(request, 7)
        return redirect('order:sales-list')

    #결제유형 콤보
    payment_typeQ = Q()
    payment_typeQ |= Q(id=13)
    payment_typeQ |= Q(id=14)
    payment_typeQ |= Q(id=15)

    #결제상태 콤보
    payment_stateQ = Q()
    payment_stateQ |= Q(id=16)
    payment_stateQ |= Q(id=17)
    
    context = {
        'pdt_combo': Product.objects.all(),
        'staff_combo': User.objects.filter(is_staff=False).exclude(staff_type=4),
        'payment_type_combo': CodeDt.objects.filter(payment_typeQ),
        'payment_state_combo': CodeDt.objects.filter(payment_stateQ),
        'client_combo': Client.objects.all(),# TODO 거래처 콤보 -> 모달 팝업
    }
    return render(request, 'order/sales-form.html', context)

def modify_sales(request, pk):
    print(request.method, 'modify-sales', pk)

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order = update(request, pk)

    #결제유형 콤보
    payment_typeQ = Q()
    payment_typeQ |= Q(id=13)
    payment_typeQ |= Q(id=14)
    payment_typeQ |= Q(id=15)

    #결제상태 콤보
    payment_stateQ = Q()
    payment_stateQ |= Q(id=16)
    payment_stateQ |= Q(id=17)

    context={
        'order': order,
        'pdt_combo': Product.objects.all(),
        'staff_combo': User.objects.filter(is_staff=False).exclude(staff_type=4),
        'payment_type_combo': CodeDt.objects.filter(payment_typeQ),
        'payment_state_combo': CodeDt.objects.filter(payment_stateQ),
        'client_combo': Client.objects.all(),#TODO 콤보-> 모달팝업
    }
    return render(request, 'order/sales-form.html', context)

def delete_sales(request, pk):
    print(request.method, 'delete_sales')
    Order.objects.get(id=pk).delete()
    return redirect('order:sales-list')

''' 충전관리 '''
def charge(request):
    context={
        'list': ''
    }
    return render(request, 'order/charge.html', context)

''' 임대관리 '''
def rental(request):
    context={
        'list': ''
    }
    return render(request, 'order/rental.html', context)

''' 미수금 내역 '''
def uncollected_amount(request):
    context={
        'list': ''
    }
    return render(request, 'order/uncollected-amount.html', context)

''' 재고 내역 '''
def stock(request):
    context={
        'list': ''
    }
    return render(request, 'order/stock.html', context)

''' 대시보드 '''
def dashboard(request):
    context={
        'list': ''
    }
    return render(request, 'order/dashboard.html', context)

''' CRUD '''
def update(request, pk):
    order = Order.objects.get(id=pk)

    # TODO 거래처는 모달 팝업에서 선택으로 바꿀예정이기에 
    client = Client.objects.get(id=request.POST.get('client'))
    staff = User.objects.get(id=request.POST.get('staff'))
    product = Product.objects.get(id=request.POST.get('product'))
    payment_type = CodeDt.objects.get(id=request.POST.get('payment_type'))
    payment_state = CodeDt.objects.get(id=request.POST.get('payment_state'))

    order.orderdate = request.POST.get('orderdate')
    order.client = client
    order.staff = staff
    order.product = product
    order.unit = request.POST.get('unit')
    order.unit_price = request.POST.get('unit_price')
    order.quantity = request.POST.get('quantity')
    order.ammount = request.POST.get('ammount')
    order.approver = request.POST.get('approver')
    order.payment_type = payment_type
    order.payment_state = payment_state
    order.comment = request.POST.get('comment')
    order.save()

    return order

def insert(request, biz_type_id):

    orderdate = request.POST.get('orderdate')
    no = '00'+str(len(Order.objects.filter(orderdate=orderdate))+1)

    Order(
        order_no = orderdate.replace("-","") + no[len(no)-3:len(no)],
        biz_type=CodeDt.objects.get(id=biz_type_id),
        orderdate=orderdate,
        client=Client.objects.get(id=request.POST.get('client')),
        staff=User.objects.get(id=request.POST.get('staff')),
        product=Product.objects.get(id=request.POST.get('product')),
        unit=request.POST.get('unit'),
        unit_price=request.POST.get('unit_price'),
        quantity=request.POST.get('quantity'),
        ammount=request.POST.get('ammount'),
        approver=request.POST.get('approver'),
        payment_type=CodeDt.objects.get(id=request.POST.get('payment_type')),
        payment_state=CodeDt.objects.get(id=request.POST.get('payment_state')),
        comment=request.POST.get('comment'),
    ).save()