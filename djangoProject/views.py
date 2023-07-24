import requests
from django.shortcuts import render

def process_string_view(request):
    result = None

    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        if input_string:
            # Send the input_string to the Flask API in ml_processor for processing
            api_url = 'http://ml_processor_app:8001/process_string'
            response = requests.post(api_url, json={'input_string': input_string})
            if response.status_code == 200:
                result = response.json().get('result')

    return render(request, 'djangoProject/index.html', {'result': result})