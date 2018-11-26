import requests, secrets, json

class Request_api:

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
                "voucher_url" : "https://mini-commerce-app.herokuapp.com/order_by/1",
                "idempotency_token": secrets.token_hex(16),
                "order_id": order_id,
                "terminal_id":terminal_id,
                "purchase_description":"Compra en Tienda X",
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

        url = 'https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/refund'
        data = { "payment_request_token" : token}
        data_request = json.dumps(data, ensure_ascii = False)
        r = requests.post(url, data = data_request, headers = self.headers)        
        response = r.json()

        response = {
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
                        "value": "13.390"
                    },
                    {
                        "name": "Arroz X 80g",
                        "value": "4.190"
                    }
                ],
                "user_ip_address": "61.1.224.56",
                "merchant_user_id": "null",
                "token": "pr-3d6a2289193bec5adb5080dc2e91cadeba29b58f06ebbba1aba4c9eb85c6777e76811dcd",
                "tpaga_payment_url": "https://w.tpaga.co/eyJtIjp7Im8iOiJQUiJ9LCJkIjp7InMiOiJtaW5pbWFsLW1hIiwicHJ0IjoicHItM2Q2YTIyODkxOTNiZWM1YWRiNTA4MGRjMmU5MWNhZGViYTI5YjU4ZjA2ZWJiYmExYWJhNGM5ZWI4NWM2Nzc3ZTc2ODExZGNkIn19",
                "status": "reverted",
                "expires_at": "2018-11-05T15:10:57.549-05:00",
                "cancelled_at": "null",
                "checked_by_merchant_at": "2018-10-22T11:26:16.964-05:00",
                "delivery_notification_at": "2018-10-22T11:29:36.017-05:00"
        }

        return response
