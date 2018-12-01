#Django utilities
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Python utilities
import json, requests, secrets
import datetime
import dateutil.parser

#Local files utilities
from .models import Order, Item 
from products.models import Product
from .request_api import Request_api
from .utilities import add_months, listing_order



@login_required
def pay_products(request):
        
        arr_items = []
        response = {}
        if request.method == "POST":

                num_products = int(request.POST["num_products"])
                data = request.POST
                total_amount = 0

                #Make purchase items array
                for i in range(num_products):
                        num = int(data["cant_product"+str(i + 1)])
                        for j in range(num):
                                product = {
                                        "name" : data["name_product"+str(i + 1)],
                                        "value" : float(
                                                data["value_product"+str(i + 1)]
                                        )
                                }
                                total_amount += product["value"]
                                arr_items.append(product)
                

                expired_date = add_months(datetime.datetime.now(), 1)
                
                make_request = Request_api()
                ip_addr = str(request.META.get("REMOTE_ADDR"))
                #Make request to TPAGA api
                response = make_request.make_pay_request(
                        total_amount,
                        arr_items, 
                        str(secrets.token_hex(6)), 
                        expired_date, 
                        "default", 
                        ip_addr
                )

                order = Order.objects.create(
                        terminal_id = response["terminal_id"], 
                        total_amount = float(response["cost"]),
                        order_token = response["order_id"],
                        status = response["status"],
                        token_response = response["token"],
                        user = request.user.client
                )
                order.save()

                for item in arr_items:
                        Item.objects.create(
                                name = item["name"],
                                value = item["value"],
                                order = order
                        ) 
        
        #Getting expires_at date and formating
        date_order = dateutil.parser.parse(
                response['expires_at']
        ).strftime("%d/%m/%y")
                
        data_list = listing_order(arr_items)

        return render(
                request,
                'products/pay_products.html',
                {
                        "data_list" : data_list,
                        "pay_link" : response["tpaga_payment_url"],
                        "data_order": response,
                        "date_order" : date_order
                } 
        )

def voucher(request, order_token):

        #getting order from order_token param 
        try:
            order = Order.objects.get_object_or_404(order_token = order_token)
        except Order.DoesNotExist:
            raise Http404
        
        #Order's items
        items_list = Item.objects.filter(order = order)
        arr_items = []
        for item in items_list:
                product = {
                        "name" : item.name,
                        "value" : item.value
                }
                arr_items.append(product)

        data_list = listing_order(arr_items)
        return render(
                request,
                'products/voucher.html',
                {
                        "order":order,
                        "data_list":data_list
                }
        )

@login_required
def confirm_pay(request, order_token):
       
        try:
            order = Order.objects.get_object_or_404(order_token = order_token)
        except Order.DoesNotExist:
            raise Http404

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

        data_list = listing_order(arr_items)
        return render(
                request,
                'payment/confirm.html',
                {
                        "data_list" : data_list,
                        "order_data" : order,
                        "response" : response
                }
        )

@login_required
def confirm_delivery(request, order_token):
        try:
            order = Order.objects.get_object_or_404(order_token = order_token)
        except Order.DoesNotExist:
            raise Http404

        request_status = Request_api()
        response = request_status.report_delivery(order.token_response)

        if order.status == "paid":
                order.status = response["status"]
                order.save()

        url = "/confirm_pay/"+order_token
        return redirect(url)


@login_required
def list_trans(request):
      
        list_order = {}
        #Listing transactions for user
        if request.method == 'POST':
                order_id = request.POST["order_id"]
                try:
                        order = Order.objects.get_object_or_404(id = order_id)
                except Order.DoesNotExist:
                        raise Http404
                
                request_status = Request_api()
                response = request_status.revert_pay(order.token_response)
                order.status = response["status"]
                order.save()
                print(response)
                messages.success(request,'transacción revertida')
                return redirect('list_trans')
        else:
                #Listing transactions for admin (all)
                if request.user.is_staff:
                        list_order = Order.objects.all()
                        list_order = list_order.order_by('id')
                else:
                        list_order = Order.objects.filter(
                                user = request.user.client
                        )
                        list_order = list_order.order_by('-date_order','id')
                
                #Pagination
                paginator = Paginator(list_order, 5)
                page = request.GET.get('page')
                list_order = paginator.get_page(page)

        return render(
                request,
                'payment/list.html',
                {
                        "list_order" : list_order
                }
        )  
        
        