from django.shortcuts import render

# Create your views here.
def call_daum_address(request):
    key = request.GET.get('key', '')

    # if key:
    #     clientlist = Client.objects.filter(cust_nm__contains=key)
    # else:
    #     clientlist = Client.objects.all()

    context={
        # 'clientpoplist': clientlist,
        'key': key,
    }

    return render(request, 'common/address.html', context)