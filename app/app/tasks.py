# tasks.py (Django project)
import time

from celery import Celery

# tasks.py (inside your Django app)

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def process_data(data):
    # Your task processing logic here
    # This function will be executed by Celery workers
    # Call the Flask ML processor to process the data
    import requests
    flask_app_url = 'http://localhost:5001/process_data'
    response = requests.post(flask_app_url, json={'data': data})
    return response.json() if response.status_code == 200 else None


