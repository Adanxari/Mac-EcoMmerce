from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact, order, OrderUpdate
from math import ceil
import json

# Create your views here.


def index(request):
    #    products= product.objects.all()
    #    n= len(products)
    #    nSlides= n//4 + ceil((n/4)-(n//4))
    #    allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    #    params={'allProds':allProds }

    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact = contact(name=name, email=email, phone=phone, desc=desc)
        Contact.save()
    return render(request, 'shop/contacts.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            Order = order.objects.filter(order_id=orderId, email=email)
            if len(Order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        {"status": "success", "updates": updates, "itemsJson": Order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if (query in item.Desctription.lower() or query in item.Product_name.lower() or query in item.category.lower()):
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    print(1, allProds)
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def productView(request, myid):
    # fatch product from db using id
    prod = product.objects.filter(id=myid)
    return render(request, 'shop/productView.html', {'product': prod[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = order(items_json=items_json, name=name, email=email, address1=address1, city=city,
                      address2=address2, state=state, zip_code=zip_code, phone=phone)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,
                             update_desc="The order has been placed")
        update.save()
        thank = True
        id = Order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
