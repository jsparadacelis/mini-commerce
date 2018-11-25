from django.shortcuts import render
from .forms import DetailForm
import json, requests, secrets
from .models import Order 
from products.models import Product

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


                        """ mr = make_request(
                                total_amount,
                                arr_items,
                                secrets.token_hex(6),
                                "calle_13"
                        ) """
                        
                        mr = {
                                "miniapp_user_token": "null",
                                "cost": "12000.0",
                                "purchase_details_url": "https://example.com/compra/348820",
                                "voucher_url": "https://example.com/comprobante/348820",
                                "idempotency_token": "ea0c78c5-e85a-48c4-b7f9-24a9014a2339",
                                "order_id": "348820",
                                "terminal_id": "sede_45",
                                "purchase_description": "Compra en Tienda X",
                                "purchase_items": [
                                        {
                                        "name": "Aceite de girasol",
                                        "value": 13390
                                        },
                                        {
                                        "name": "Arroz X 80g",
                                        "value": 4190
                                        }
                                ],
                                "user_ip_address": "61.1.224.56",
                                "merchant_user_id": "null",
                                "token": "pr-39394abaed1d3e97d1fe67423079c36336905671bb5a77877e3b9dc032a3070c52162365",
                                "tpaga_payment_url": "https://w.tpaga.co/eyJtIjp7Im8iOiJQUiJ9LCJkIjp7InMiOiJtaW5pbWFsLW1hIiwicHJ0IjoicHItMzkzOTRhYmFlZDFkM2U5N2QxZmU2NzQyMzA3OWMzNjMzNjkwNTY3MWJiNWE3Nzg3N2UzYjlkYzAzMmEzMDcwYzUyMTYyMzY1In19",
                                "status": "created",
                                "expires_at": "2018-11-05T15:10:57.549-05:00",
                                "cancelled_at": "null",
                                "checked_by_merchant_at": "null",
                                "delivery_notification_at": "null"
                        }


                        print(mr)

                        order = Order.objects.create(
                                terminal_id = mr["terminal_id"], 
                                total_amount = float(mr["cost"]),
                                order_token = mr["order_id"],
                                items = mr["purchase_items"],
                                status = mr["status"]
                        ) 

        
        return render(
                request,
                'products/generic.html',
                {
                        "pay_url":mr["tpaga_payment_url"]
                }
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
