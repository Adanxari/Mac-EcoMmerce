from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact, order
from math import ceil

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
        params = {'allProds':allProds}
    return render(request,"shop/index.html", params)


def about (request):
    return render(request,'shop/about.html')

def contacts (request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact = contact(name=name, email=email, phone=phone, desc=desc)
        Contact.save()    
    return render(request,'shop/contacts.html')

def tracker (request):
    return render(request,'shop/tracker.html')

def search (request):
    return render(request,'shop/search.html')

def productView (request, myid):
    #fatch product using id
    prod = product.objects.filter(id=myid)
    return render(request,'shop/productView.html',{'product':prod[0]})

def checkout (request):
    if request.method=="POST":
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
                       address2=address2,state=state, zip_code=zip_code, phone=phone)
        Order.save()
        thank = True
        id = Order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')