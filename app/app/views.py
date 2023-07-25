import requests
from django.shortcuts import render


# views.py (in your Django app)

from django.http import JsonResponse
from celery import shared_task


from django.http import JsonResponse
from celery import shared_task

@shared_task
def process_string_task(input_string):
    # Send the input_string to the ml_processor app for processing
    # You can use requests or any other library to send the request
    # Replace "http://ml_processor_app:8001/process_string" with the actual URL of ml_processor app
    response = requests.post("http://ml_processor_app:8001/process_string", json={'input_string': input_string})
    if response.status_code == 200:
        result = response.json().get('result')
        return result
    else:
        return None

def send_task_view(request):
    input_string = "Hello, World!"  # Replace with your data

    # Send the input_string to the Celery task for processing
    result = process_string_task.delay(input_string)
    result_data = result.get() if result else None

    return JsonResponse({'result': result_data})
