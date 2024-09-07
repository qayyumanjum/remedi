from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import generate_key, encrypt_data, decrypt_data

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