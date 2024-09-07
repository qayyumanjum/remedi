from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import generate_key, encrypt_data, decrypt_data
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import stripe

def generate_key_view(request):
    key = generate_key()
    return JsonResponse({'key': key.decode()})

@csrf_exempt
def encrypt_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        key = data.get('key').encode()
        plaintext = data.get('data')
        encrypted_data = encrypt_data(key, plaintext)
        return JsonResponse({'encrypted_data': encrypted_data.decode()})

@csrf_exempt
def decrypt_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        key = data.get('key').encode()
        encrypted_data = data.get('encrypted_data').encode()
        decrypted_data = decrypt_data(key, encrypted_data)
        return JsonResponse({'decrypted_data': decrypted_data})

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(request):
    return render(request, 'payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'T-shirt',
                        },
                        'unit_amount': 2000,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:8000/success/',
                cancel_url='http://localhost:8000/cancel/',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success_view(request):
    return render(request, 'success.html')

def cancel_view(request):
    return render(request, 'cancel.html')
