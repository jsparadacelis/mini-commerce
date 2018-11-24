from django.shortcuts import render
from .forms import PayForm
import json

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
        purchase_item = json.dumps(arr_items, ensure_ascii=False)
        data_request = {
                "cost" : cost,
                "purchase_details_url" : "http://127.0.0.1:8000/content/1",
                "voucher_url" : "http://127.0.0.1:8000/content/1",
                
        }

        return render(request,'products/generic.html')

def content(request):
        return render(request,'products/elements.html')
        
        

            
            
    
    
