import requests, secrets, json

class Request_api:

    #Headers for requests to api
    def __init__(self):
        self.headers = {
                'Authorization': 'Basic bWluaWFwcC1nYXRvMzptaW5pYXBwbWEtMTIz',
                'Cache-Control': 'no-cache',
                'Content-Type':'application/json'
        }

    

    def make_pay_request(self, total_amount, arr_items, order_id, expired_date, terminal_id, ip_addr):
        data_request = {
                "cost" : int(total_amount),
                "purchase_details_url" : "https://mini-commerce-app.herokuapp.com/confirm_pay/"+order_id,
                "voucher_url" : "https://mini-commerce-app.herokuapp.com/voucher/"+order_id,
                "idempotency_token": secrets.token_hex(16),
                "order_id": order_id,
                "terminal_id":terminal_id,
                "purchase_description":"Compra en Tienda Phantom",
                "purchase_items": arr_items,
                "user_ip_address": ip_addr,
                "expires_at": expired_date
        }

        data_request = json.dumps(data_request, ensure_ascii = False)
        url = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/create'
        r = requests.post(url, data = data_request, headers = self.headers)        
        response = r.json() 

        return response

        
    def confirm_pay_status(self, token):

        url = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/'+token+'/info'
        r = requests.get(url, headers  = self.headers)
        response = r.json() 


        return response
    
    def report_delivery(self, token):

        url = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/confirm_delivery'
        data = { "payment_request_token" : token}
        data_request = json.dumps(data, ensure_ascii = False)
        r = requests.post(url, data = data_request, headers = self.headers)        
        response = r.json()

        return response

    def revert_pay(self, token):

        """ url = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/refund'
        data = { "payment_request_token" : token}
        data_request = json.dumps(data, ensure_ascii = False)
        r = requests.post(url, data = data_request, headers = self.headers)        
        response = r.json() """

        response =  {
            "status" : "reverted"
        }

        return response
