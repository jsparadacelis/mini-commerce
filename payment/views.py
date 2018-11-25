from django.shortcuts import render
from .forms import DetailForm
import json, requests, secrets
from .models import Order 
from products.models import Product, Item

def pay_products(request):
        if request.method == "POST":
                form = DetailForm(request.POST)
                print('hello')
                if form.is_valid():
                        data = form.cleaned_data
                        arr_items = []
                        for i in range(int(data["cant_product"])):
                                product = {
                                        "name": data["name_product"],
                                        "value" : data["value_product"]
                                }
                                arr_items.append(product)  

                        total_amount = data["value_product"] * int(data["cant_product"])

                        product = Product.objects.get(
                                name = data["name_product"]
                        )

                        order = Order.objects.create(
                                terminal_id = "calle_13", 
                                total_amount = total_amount
                        )

                        item = Item.objects.create(
                                product = product,
                                order = order,
                                cant = int(data["cant_product"]),
                                total_amount = data["value_product"]
                        )


                        mr = make_request(
                                total_amount,
                                arr_items,
                                str(order.id),
                                order.terminal_id
                        )
                        

        
        return render(
                request,
                'products/generic.html',
        )

def detail_products(request):
    if request.method == "POST":
        form = DetailForm(request.POST)
        arr_items = list()
        data = dict()
        total_amount = 0
        if form.is_valid():
            data = form.cleaned_data
            total_amount = data["value_product"] * int(data["cant_product"])   
       
        
        return render(
                request,
                'products/generic.html',
                {
                        #"url_pago": response["tpaga_payment_url"],
                        "data" : data,
                        "total" : total_amount
                }
        )


def make_request(total_amount, arr_items, order_id, terminal_id):
        data_request = {
                "cost" : total_amount,
                "purchase_details_url" : "https://mini-commerce-app.herokuapp.com/content/1",
                "voucher_url" : "https://mini-commerce-app.herokuapp.com/content/1",
                "idempotency_token": secrets.token_hex(16),
                "order_id": order_id,
                "terminal_id":terminal_id,
                "purchase_description":"Compra en Tienda X",
                "purchase_items": arr_items,
                "user_ip_address":"61.1.224.56",
                "expires_at":"2018-12-05T20:10:57.549653+00:00"
        }

        data_request = json.dumps(data_request, ensure_ascii=False)
        headers = {
                'Authorization': 'Basic bWluaWFwcC1nYXRvMzptaW5pYXBwbWEtMTIz',
                'Cache-Control': 'no-cache',
                'Content-Type':'application/json'
        }
        url = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/create'
        r = requests.post(url, data = data_request, headers = headers)        
        
        response = r.json() 

        return response
        
        
def order_by(request, id):
        order = Order.objects.get(id=id)
        items = Item.objects.filter(order = order)
        return render(
                request,
                'payment/detail.html',
                {
                        "order":order,
                        "list_items":items
                }
        )
