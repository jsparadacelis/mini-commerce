from django.shortcuts import render
from .forms import PayForm
import json, requests, secrets

def pay_products(request):
    if request.method == "POST":
        form = PayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            arr_items = list()
            cost = 0
            for i in range(int(data["cant_product"])):
                product = {
                        "name": data["name_product"],
                        "value" : data["value_product"]
                }
                cost += data["value_product"]
                arr_items.append(product)
        
        data_request = {
                "cost" : cost,
                "purchase_details_url" : "https://mini-commerce-app.herokuapp.com/content/1",
                "voucher_url" : "https://mini-commerce-app.herokuapp.com/content/1",
                "idempotency_token": secrets.token_hex(16),
                "order_id":"348820",
                "terminal_id":"sede_45",
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

        return render(
                request,
                'products/generic.html',
                {
                        "url_pago": response["tpaga_payment_url"]
                }
                )

def content(request):
        return render(request,'products/elements.html')
        
        

            
            
    
    
