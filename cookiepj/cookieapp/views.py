from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cookie(request):
    print(request.COOKIES)
    still = request.COOKIES.get('nay', None)
    resp = HttpResponse('In a view- the nay cookie value is ' + str(still))
    if still :
        resp.set_cookie('nay', + int(still) + 1)  #No expired data until broswer close
    else:
        resp.set_cookie('nay', 443) #No expired data until broswer close
    resp.set_cookie('linn', 500, max_age=1000)
    return resp


def sessfun(request):
    count_lists = request.session.get('count_lists',0) +1
    request.session['count_lists'] = count_lists
    if count_lists >= 4 :del(request.session['count_lists'])
    resp = HttpResponse('Counting =' + str(count_lists))
    resp.set_cookie('nay_linn_oo',404 ,max_age=10000)
    return resp
    