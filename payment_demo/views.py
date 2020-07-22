import uuid

from django.shortcuts import render
from square.client import Client



def payment(request):
    if request.method=='POST':
        client = Client(
            access_token='EAAAEBltDePV9iY0DTDR0lbwFKz3yWo53rQYb2j_F_xJCdg-rpu6amh-noG_sSaC',
            environment='sandbox',
        )
        payments_api = client.payments
        body = {}
        body['source_id'] = request.POST['nonce']
        body['idempotency_key'] = str(uuid.uuid1())
        body['amount_money'] = {}
        body['amount_money']['amount'] = 200
        body['amount_money']['currency'] = 'USD'

        result = payments_api.create_payment(body)
        if result.is_success():
            print('--------------------',result.body)
        elif result.is_error():
            print('+++++++++++++++++++',result.errors)
    return render(request, 'payment_demo/payment.html')