#Django utilities
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


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
def make_order(request):
        
        arr_items = []
        response = {}
        if request.method == "POST" :
                
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
                
                make_request = Request_api()
                ip_addr = str(request.META.get("REMOTE_ADDR"))
                expired_date = add_months(datetime.datetime.now(), 1)

                response = make_request.make_pay_request(
                        total_amount,
                        arr_items, 
                        str(secrets.token_hex(6)), 
                        expired_date, 
                        "default", 
                        ip_addr
                )
                
                if "error_code" in response:
                        messages.error(
                                request,
                                'No se pudo completar la transacción'
                        )
                        return redirect("list_products")

                order = Order.objects.create(
                        terminal_id = response["terminal_id"], 
                        total_amount = float(response["cost"]),
                        order_token = response["order_id"],
                        status = response["status"],
                        token_response = response["token"],
                        client = request.user.client,
                        payment_link = response["tpaga_payment_url"]
                )
                order.save()

                for item in arr_items:
                        Item.objects.create(
                                name = item["name"],
                                value = item["value"],
                                order = order
                        ) 
                
                return redirect('/pay_products/'+str(order.id))


class confirm_pay(LoginRequiredMixin, DetailView):
        template_name = "payment/confirm.html"
        def get(self, request, order_token):
                try:
                        order = Order.objects.get(order_token = order_token)
                except Order.DoesNotExist:
                        raise Http404
                
                request_status = Request_api()
                response = request_status.confirm_pay_status(order.token_response)

                if "error_code" in response:
                        messages.error(
                                request,
                                'No se pudo completar la transacción'
                        )
                        return redirect("list_products")

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
                        self.template_name,
                        {
                                'order_data': order,
                                'data_list' : data_list
                        }
                )


@login_required
def confirm_delivery(request, order_token):
        try:
            order = Order.objects.get(order_token = order_token)
        except Order.DoesNotExist:
            raise Http404

        request_status = Request_api()
        response = request_status.report_delivery(order.token_response)
        if "error_code" in response:
                        messages.success(
                                request,
                                'No se pudo completar la transacción'
                        )
                        return redirect("list_products")

        if order.status == "paid":
                order.status = response["status"]
                order.save()

        url = "/confirm_pay/"+order_token
        return redirect(url)


class list_trans(LoginRequiredMixin, ListView):
        
        template_name = "payment/list.html"
        def get(self, request):
                if request.user.is_staff:
                        list_order = Order.objects.all()
                        list_order = list_order.order_by('id')
                else:
                        list_order = Order.objects.filter(
                                client = request.user.client
                        )
                        list_order = list_order.order_by('-modified_date','id')
                
                #Pagination
                paginator = Paginator(list_order, 5)
                page = request.GET.get('page')
                list_order = paginator.get_page(page)
                
                return render(
                        request,
                        self.template_name,
                        {
                                "list_order" : list_order
                        }
                )

@login_required
def revert_order(request):
      
        if request.method == 'POST':
                order_id = request.POST["order_id"]
                try:
                        order = Order.objects.get(id = order_id)
                except Order.DoesNotExist:
                        raise Http404
                
                request_status = Request_api()
                response = request_status.revert_pay(order.token_response)
                if "error_code" in response:
                        messages.error(
                                request,
                                'No se pudo completar la transacción'
                        )
                        return redirect("list_trans")

                order.status = response["status"]
                order.save()
                messages.success(request,'transacción revertida')
                return redirect('list_trans')


class pay_products(LoginRequiredMixin, DetailView):
    template_name = "products/pay_products.html"
    def get(self, request, pk):
        try:
                order = Order.objects.get(pk = pk)
        except Order.DoesNotExist:
                raise Http404,

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
                self.template_name,
                {
                        'order_data': order,
                        'data_list' : data_list
                }
        )

