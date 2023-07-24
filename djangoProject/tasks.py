# djangoProject/your_django_app/tasks.py

from djangoProject.celery import celery_app

@celery_app.task
def process_ml_data(data):
    # Call the task from the ml_processor project (plain Python)
    # The task in ml_processor should be defined as a regular function
    result = your_ml_processor_function(data)
    return result
