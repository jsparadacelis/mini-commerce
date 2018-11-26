from django.shortcuts import render, redirect
from .forms import DetailForm
import json, requests, secrets
from .models import Order, Item 
from products.models import Product
from .request_api import Request_api
from .expired_date import add_months
import datetime
import dateutil.parser

from django.http import HttpResponse

import itertools
from operator import itemgetter

def pay_products(request):
        
        arr_items = []
        pay_link = ""
        data_order_request = {}
        if request.method == "POST":
                list_products = request.POST
                total_amount = 0
                list_item = list_products["data"].split(",")
                
                for i in range(int(len(list_item)/2)):
                        product = {
                                "name" : list_item.pop(0),
                                "value" : float(list_item.pop(0))
                        }
                        total_amount += product["value"]
                        arr_items.append(product)
                

                expired_date = add_months(datetime.datetime.now(), 1)
                
                make_request = Request_api()
                ip_addr = str(request.META.get("REMOTE_ADDR"))
                print(ip_addr)
                response = make_request.make_pay_request(total_amount, arr_items, str(secrets.token_hex(6)), expired_date,  'sede_45', ip_addr)
                data_order_request = response

                print(response)

                pay_link = response["tpaga_payment_url"]
                print(data_order_request)
                order = Order.objects.create(
                        terminal_id = response["terminal_id"], 
                        total_amount = float(response["cost"]),
                        order_token = response["order_id"],
                        status = response["status"],
                        token_response = response["token"]
                ) 
                for item in arr_items:
                        Item.objects.create(
                                name = item["name"],
                                value = item["value"],
                                order = order
                        ) 
        else:
                pass


        data_list = []
        arr_items = sorted(arr_items, key = itemgetter('name'))
        for key, group in itertools.groupby(arr_items, key = lambda x : x['name']):
                l = list(group)
                d = l[0]
                data = {
                        "name" : key,
                        "quantity" : len(l),
                        "value" : d["value"],
                        "url" : Product.objects.get(name = key).image.url
                }
                data_list.append(data)
                
        date = dateutil.parser.parse(data_order_request['expires_at']).strftime("%d/%m/%y")
        return render(
                request,
                'products/generic.html',
                {
                        "data_list" : data_list,
                        "pay_link" : pay_link,
                        "data_order": data_order_request,
                        "date_order" : date
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

def confirm_pay(request, order_token):
        print()
        order = Order.objects.get(order_token = order_token)
        request_status = Request_api()
        response = request_status.confirm_pay_status(order.token_response)

        if order.status == "created":
                order.status = response["status"]
                order.save()

        items_list = Item.objects.filter(order = order)
        arr_items = []
        for item in items_list:
                product = {
                        "name" : item.name,
                        "value" : item.value
                }
                arr_items.append(product)

        data_list = []
        arr_items = sorted(arr_items, key = itemgetter('name'))

        for key, group in itertools.groupby(arr_items, key = lambda x : x['name']):
                l = list(group)
                d = l[0]
                data = {
                        "name" : key,
                        "quantity" : len(l),
                        "value" : d["value"],
                        "url" : Product.objects.get(name = key).image.url
                }
                data_list.append(data)


        print(data_list)
        return render(
                request,
                'payment/confirm.html',
                {
                        "data_list" : data_list,
                        "order_data" : order
                }
        )

def confirm_delivery(request, order_token):
        order = Order.objects.get(order_token = order_token)
        request_status = Request_api()
        response = request_status.report_delivery(order.token_response)

        if order.status == "paid":
                order.status = response["status"]
                order.save()

        url = "/confirm_pay/"+order_token
        return redirect(url)

def list_trans(request):

        
        list_order = Order.objects.all()
        return render(
                request,
                'payment/list.html'
        )